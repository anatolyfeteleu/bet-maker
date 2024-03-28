from fastapi import FastAPI

from src.events.routers import router as events_router
from src.predictions.routers import router as predictions_router

app = FastAPI(title="Bet Maker", debug=True)

app.include_router(
    router=predictions_router,
    prefix="/bets",
)
app.include_router(router=events_router, prefix="/events")
