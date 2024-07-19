from fastapi import FastAPI, APIRouter, HTTPException
from models import BattingType

tag_definitions = [
    {
        "name": "data",
        "description": "Information related to rules, game mechanics, etc.",
    },
    {
        "name": "games",
        "description": "Information about current and past games and plate appearances.",
    },
    {"name": "players", "description": "Information about players."},
    {
        "name": "teams",
        "description": "Information about teams and their ballparks.",
    },
]

app = FastAPI(
    title="MLR-Reference API",
    summary="The MLR-Reference API allows users to access league data (players, games, teams, etc.) from the MLR database.",
    description="For issues, please contact Sterling Turlington on the MLR Main Discord (@veritablequandary).",
    version="0.0.1",
    docs_url="/",
    redoc_url=None,
    openapi_tags=tag_definitions,
)

dataRouter = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={
        404: {"description": "The requested resource was not found."},
        500: {"description": "Internal server error."},
    },
)


@dataRouter.get("/battingTypes/all", status_code=200, tags=["data"])
async def get_all_batting_types():
    battingTypes = BattingType.select()
    if len(battingTypes) == 0:
        raise HTTPException(status_code=404, detail="No batting types found.")
    return battingTypes


app.include_router(dataRouter)
