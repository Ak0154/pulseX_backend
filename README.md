# 🚀 PulseX Backend API

**PulseX** is a secure and high-performance backend system built with **FastAPI** and **MongoDB** for real-time cryptocurrency data retrieval and user authentication.  
It integrates **JWT-based authentication**, **bcrypt password hashing**, and live data from the **CoinMarketCap API** to deliver a scalable and modern crypto backend solution.

---

## 🧩 Features

- 🔒 **User Authentication** — Secure signup and login using JWT access tokens.  
- 🧠 **Hashed Passwords** — Passwords are encrypted using Bcrypt for enhanced security.  
- ⚡ **Asynchronous Architecture** — Built entirely with FastAPI async support and Motor (async MongoDB driver).  
- 💰 **Live Crypto Data** — Fetches real-time cryptocurrency listings and price information from CoinMarketCap.  
- 🧱 **Modular Design** — Easy to maintain and extend with separate modules for routes, models, and services.  
- 🧾 **Environment-Based Configuration** — Uses `.env` for secret keys, database URLs, and API keys.  

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | FastAPI |
| **Database** | MongoDB (Motor AsyncIO driver) |
| **Authentication** | JWT (JSON Web Tokens) |
| **Password Security** | Bcrypt Hashing |
| **Async HTTP Client** | HTTPX |
| **External API** | CoinMarketCap API |

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/Ak0154/PulseX-Backend-API.git
cd pulseX_backend
uvicorn main:app --reload
