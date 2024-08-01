from fastapi import FastAPI
from routers.data import dataRouter
from routers.games import gamesRouter

tags = [
    {
        "name": "calculators",
    },
    {
        "name": "data",
    },
    {
        "name": "games",
    },
    {
        "name": "players",
    },
    {
        "name": "teams",
    },
]

app = FastAPI(
    title="MLR-Reference API",
    summary="The MLR-Reference API allows users to access read-only data from the MLR database.",
    description="For issues, please contact Sterling Turlington on the MLR Main Discord (@veritablequandary).",
    version="1.0.0",
    docs_url="/",
    redoc_url=None,
    openapi_tags=tags,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.include_router(dataRouter)
app.include_router(gamesRouter)
