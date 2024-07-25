from fastapi import FastAPI, APIRouter, HTTPException
from models import BattingType, PitchingType, HandBonus, BattingPitchingTypeDefinition

####################
# Tag definitions (docs)
####################

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

####################
# API instance
####################

app = FastAPI(
    title="MLR-Reference API",
    summary="The MLR-Reference API allows users to access league data (players, games, teams, etc.) from the MLR database.",
    description="For issues, please contact Sterling Turlington on the MLR Main Discord (@veritablequandary).",
    version="0.0.1",
    docs_url="/",
    redoc_url=None,
    openapi_tags=tag_definitions,
)

####################
# Routers
####################

dataRouter = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={
        404: {"description": "The requested resource was not found."},
        500: {"description": "Internal server error."},
    },
)

####################
# /data/battingTypes
####################


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
    "/battingTypes/search",
    tags=["data"],
    description="Search for one or more batting types using a comma-separated list of IDs.",
    response_description="A list of data for all matching batting types; if no search terms provided, all batting types will be returned.",
)
def search_batting_types(ids: str | None = None) -> list[BattingPitchingTypeDefinition]:
    if (ids) != None:
        separated = list(map(str.upper, ids.split(",")))
        battingTypes = (
            BattingType.select()
            .where(BattingType.type.in_(separated))
            .order_by(BattingType.type)
            .dicts()
        )
        if len(battingTypes) == 0:
            raise HTTPException(status_code=404, detail="No batting types found.")
        return [*battingTypes]
    else:
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


####################
# /data/pitchingTypes
####################


@dataRouter.get(
    "/pitchingTypes/all",
    tags=["data"],
    description="Data on all current pitching types.",
    response_description="A list of data on all current pitching types, sorted by type ID.",
)
def get_all_pitching_types() -> list[BattingPitchingTypeDefinition]:
    pitchingTypes = PitchingType.select().order_by(PitchingType.type).dicts()
    if len(pitchingTypes) == 0:
        raise HTTPException(status_code=404, detail="No pitching types found.")
    return [*pitchingTypes]


@dataRouter.get(
    "/pitchingTypes/search",
    tags=["data"],
    description="Search for one or more pitching types using a comma-separated list of IDs.",
    response_description="A list of data for all matching pitching types; if no search terms provided, all batting types will be returned.",
)
def search_pitching_types(
    ids: str | None = None,
) -> list[BattingPitchingTypeDefinition]:
    if (ids) != None:
        separated = list(map(str.upper, ids.split(",")))
        pitchingTypes = (
            PitchingType.select()
            .where(PitchingType.type.in_(separated))
            .order_by(PitchingType.type)
            .dicts()
        )
        if len(pitchingTypes) == 0:
            raise HTTPException(status_code=404, detail="No pitching types found.")
        return [*pitchingTypes]
    else:
        pitchingTypes = PitchingType.select().order_by(PitchingType.type).dicts()
        if len(pitchingTypes) == 0:
            raise HTTPException(status_code=404, detail="No pitching types found.")
        return [*pitchingTypes]


@dataRouter.get(
    "/pitchingTypes/{id}",
    tags=["data"],
    description="Data on a specific pitching type.",
    response_description="Data on the specific pitching type",
)
def get_pitching_type(id: str) -> BattingPitchingTypeDefinition:
    pitchingType = PitchingType.get_or_none(PitchingType.type == id.upper())
    if (pitchingType) == None:
        raise HTTPException(status_code=404, detail="Pitching type not found.")
    return pitchingType


####################
# /data/handBonuses
####################


@dataRouter.get(
    "/handBonuses/all",
    tags=["data"],
    description="Data on all current pitching hand bonuses.",
    response_description="A list of data on all current pitching hand bonuses, sorted by type ID.",
)
def get_all_hand_bonuses() -> list[BattingPitchingTypeDefinition]:
    handBonuses = HandBonus.select().order_by(HandBonus.type).dicts()
    if len(handBonuses) == 0:
        raise HTTPException(status_code=404, detail="No pitching hand bonuses found.")
    return [*handBonuses]


@dataRouter.get(
    "/handBonuses/search",
    tags=["data"],
    description="Search for one or more pitching hand bonuses using a comma-separated list of IDs.",
    response_description="A list of data for all matching pitching hand bonuses; if no search terms provided, all hand bonuses will be returned.",
)
def search_hand_bonuses(
    ids: str | None = None,
) -> list[BattingPitchingTypeDefinition]:
    if (ids) != None:
        separated = list(map(str.upper, ids.split(",")))
        handBonuses = (
            HandBonus.select()
            .where(HandBonus.type.in_(separated))
            .order_by(HandBonus.type)
            .dicts()
        )
        if len(handBonuses) == 0:
            raise HTTPException(
                status_code=404, detail="No pitching hand bonuses found."
            )
        return [*handBonuses]
    else:
        handBonuses = HandBonus.select().order_by(HandBonus.type).dicts()
        if len(handBonuses) == 0:
            raise HTTPException(
                status_code=404, detail="No pitching hand bonuses found."
            )
        return [*handBonuses]


@dataRouter.get(
    "/handBonuses/{id}",
    tags=["data"],
    description="Data on a specific pitching hand bonus.",
    response_description="Data on the specific pitching hand bonus",
)
def get_hand_bonus(id: str) -> BattingPitchingTypeDefinition:
    handBonus = HandBonus.get_or_none(HandBonus.type == id.upper())
    if (handBonus) == None:
        raise HTTPException(status_code=404, detail="Pitching hand bonus not found.")
    return handBonus


app.include_router(dataRouter)
