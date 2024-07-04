from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="MLR-Reference API",
    summary="The MLR-Reference API allows users to access league data (players, games, teams, etc.) from the MLR database.",
    description="For issues, please contact Sterling Turlington on the MLR Main Discord (@veritablequandary).",
    version="0.0.1",
    docs_url="/",
    redoc_url=None,
)
