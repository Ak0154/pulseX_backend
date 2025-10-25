import httpx
from app.core.config import settings

BASE_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency"

async def get_top_cryptos(limit: int = 10):
    url = f"{BASE_URL}/listings/latest"
    headers = {"X-CMC_PRO_API_KEY": settings.COIN_API_KEY}
    params = {"limit": limit, "convert": "USD"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])


async def get_crypto_price(symbol: str):
    url = f"{BASE_URL}/quotes/latest"
    headers = {"X-CMC_PRO_API_KEY": settings.COIN_API_KEY}
    params = {"symbol": symbol.upper(), "convert": "USD"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        quote = data.get("data", {}).get(symbol.upper(), {}).get("quote", {}).get("USD", {})
        return quote.get("price")
