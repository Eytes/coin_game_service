from fastapi import FastAPI

from .routers import router_v1

app = FastAPI(title="Coin game API")
app.include_router(router_v1)
