from fastapi import FastAPI, APIRouter, HTTPException
from models import BattingType, PitchingType, BattingPitchingTypeDefinition

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


@dataRouter.get(
    "/battingTypes/all",
    tags=["data"],
    description="Data on all current batting types.",
    response_description="A list of data on all current batting types, sorted by type ID.",
)
def get_all_batting_types() -> list[BattingPitchingTypeDefinition]:
    battingTypes = BattingType.select().order_by(BattingType.type).dicts()
    if len(battingTypes) == 0:
        raise HTTPException(status_code=404, detail="No batting types found.")
    return [*battingTypes]


@dataRouter.get(
    "/battingTypes/{id}",
    tags=["data"],
    description="Data on a specific batting type.",
    response_description="Data on the specific batting type",
)
def get_batting_type(id: str) -> BattingPitchingTypeDefinition:
    battingType = BattingType.get_or_none(BattingType.type == id.upper())
    if (battingType) == None:
        raise HTTPException(status_code=404, detail="Batting type not found.")
    return battingType


@dataRouter.get(
    "/battingTypes/search",
    tags=["data"],
    description="Search for one or more batting types using a comma-separated list of IDs.",
    response_description="A list of data for all matching batting types; if no search terms provided, all batting types will be returned.",
)
def search_batting_types(ids: str | None = None) -> list[BattingPitchingTypeDefinition]:
    if (ids) != None:
        separated = list(map(str.upper(), ids.split(",")))
        battingTypes = (
            BattingType.select().where(BattingType.type.in_(separated))order_by(BattingType.type).dicts()
        )
        if len(battingTypes) == 0:
            raise HTTPException(status_code=404, detail="No batting types found.")
        return [*battingTypes]
    else:
        battingTypes = BattingType.select().order_by(BattingType.type).dicts()
        if len(battingTypes) == 0:
            raise HTTPException(status_code=404, detail="No batting types found.")
        return [*battingTypes]


app.include_router(dataRouter)