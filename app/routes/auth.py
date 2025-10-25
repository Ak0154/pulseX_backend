from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr
from app.db.mongo import db
from app.core.security import hash_password, verify_password, create_access_token
from jose import JWTError, jwt
from app.core.config import settings

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# =========================
# SCHEMAS
# =========================
class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    username: str
    email: EmailStr

# =========================
# DEPENDENCIES
# =========================
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await db.users.find_one({"email": email})
    if not user:
        raise credentials_exception
    return user

# =========================
# ROUTES
# =========================

@router.post("/register", status_code=201, response_model=UserOut)
async def register_user(user: UserRegister):
    print(f"Received password: {user.password[:50]}")  # Debug line
    print(f"Password length: {len(user.password)}") 
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_dict = user.dict()
    user_dict["hashed_password"] = hash_password(user.password)
    del user_dict["password"]

    await db.users.insert_one(user_dict)
    return UserOut(**user_dict)


@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db.users.find_one({"email": form_data.username})
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token = create_access_token({"sub": user["email"]})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserOut)
async def get_me(current_user: dict = Depends(get_current_user)):
    return UserOut(**current_user)
