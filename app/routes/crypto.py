from fastapi import APIRouter, Depends, HTTPException
from app.routes.auth import get_current_user
from app.services.coinmarket import get_top_cryptos, get_crypto_price

router = APIRouter()

@router.get("/listings")
async def get_top_cryptos_route(limit: int = 10, user: dict = Depends(get_current_user)):
    """
    Returns top 'limit' cryptocurrencies with their prices.
    Requires user authentication.
    """
    try:
        data = await get_top_cryptos(limit)
        return {"count": limit, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/price/{symbol}")
async def get_price_route(symbol: str, user: dict = Depends(get_current_user)):
    """
    Returns current price of a specific cryptocurrency by symbol.
    Example: /crypto/price/BTC
    """
    try:
        data = await get_crypto_price(symbol)
        if not data:
            raise HTTPException(status_code=404, detail=f"No data found for {symbol}")
        return {"symbol": symbol.upper(), "price": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
