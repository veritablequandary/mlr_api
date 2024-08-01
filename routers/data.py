from fastapi import APIRouter, HTTPException
from models.batting_type import *
from models.pitching_type import *
from models.hand_bonus import *
from models.season import *

####################
# /data router
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
    "/battingTypes", tags=["data"], summary="", description="", response_description=""
)
def get_all_batting_types() -> list[BattingTypeDefinition]:
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
def search_batting_types(ids: str | None = None) -> list[BattingTypeDefinition]:
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
def get_batting_type(id: str) -> BattingTypeDefinition:
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
def get_all_pitching_types() -> list[PitchingTypeDefinition]:
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
) -> list[PitchingTypeDefinition]:
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
def get_pitching_type(id: str) -> PitchingTypeDefinition:
    pitchingType = PitchingType.get_or_none(PitchingType.type**id)
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
def get_all_hand_bonuses() -> list[HandBonusDefinition]:
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
) -> list[HandBonusDefinition]:
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
def get_hand_bonus(id: str) -> HandBonusDefinition:
    handBonus = HandBonus.get_or_none(HandBonus.type**id)
    if (handBonus) == None:
        raise HTTPException(status_code=404, detail="Pitching hand bonus not found.")
    return handBonus


####################
# /data/currentSeason
####################


@dataRouter.get(
    "/currentSeason",
    tags=["data"],
    description="Returns the current season and session numbers for MLR and MiLR.",
    response_description="Season and session numbers for the MLR and MiLR leagues.",
)
def get_current_season() -> list[SeasonDefinition]:
    seasons = Season.select().order_by(Season.league).dicts()
    if len(seasons) == 0:
        raise HTTPException(status_code=404, detail="No current season data found.")
    return [*seasons]
