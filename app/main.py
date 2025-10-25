from fastapi import FastAPI
from app.routes import auth, crypto

app = FastAPI(title="Crypto Dashboard API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(crypto.router, prefix="/crypto", tags=["Crypto"])


@app.get("/")
def index():
    return ("Hi, AKASH")