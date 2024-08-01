from typing import Annotated
from fastapi import APIRouter, HTTPException, Path
from models.batting_type import *
from models.pitching_type import *
from models.hand_bonus import *
from models.season import *

dataRouter = APIRouter(
    prefix="/data",
    tags=["data"],
)


@dataRouter.get(
    "/battingTypes",
    tags=["data"],
)
def get_all_batting_types() -> list[BattingTypeDefinition]:
    battingTypes = BattingType.select().order_by(BattingType.type).dicts()
    if len(battingTypes) == 0:
        raise HTTPException(status_code=404, detail="No batting types found.")
    return [*battingTypes]


@dataRouter.get(
    "/battingTypes/{ids}",
    tags=["data"],
)
def search_batting_types(
    ids: Annotated[
        str,
        Path(
            title="A single type ID or comma-separated list of type IDs to return, e.g. HK or BC,SF,MH"
        ),
    ]
) -> list[BattingTypeDefinition]:
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
)
def get_batting_type(id: str) -> BattingTypeDefinition:
    battingType = BattingType.get_or_none(BattingType.type == id.upper())
    if (battingType) == None:
        raise HTTPException(status_code=404, detail="Batting type not found.")
    return battingType


@dataRouter.get(
    "/pitchingTypes",
    tags=["data"],
)
def get_all_pitching_types() -> list[PitchingTypeDefinition]:
    pitchingTypes = PitchingType.select().order_by(PitchingType.type).dicts()
    if len(pitchingTypes) == 0:
        raise HTTPException(status_code=404, detail="No pitching types found.")
    return [*pitchingTypes]


@dataRouter.get(
    "/pitchingTypes/search",
    tags=["data"],
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
)
def get_pitching_type(id: str) -> PitchingTypeDefinition:
    pitchingType = PitchingType.get_or_none(PitchingType.type**id)
    if (pitchingType) == None:
        raise HTTPException(status_code=404, detail="Pitching type not found.")
    return pitchingType


@dataRouter.get(
    "/handBonuses/all",
    tags=["data"],
)
def get_all_hand_bonuses() -> list[HandBonusDefinition]:
    handBonuses = HandBonus.select().order_by(HandBonus.type).dicts()
    if len(handBonuses) == 0:
        raise HTTPException(status_code=404, detail="No pitching hand bonuses found.")
    return [*handBonuses]


@dataRouter.get(
    "/handBonuses/search",
    tags=["data"],
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
)
def get_hand_bonus(id: str) -> HandBonusDefinition:
    handBonus = HandBonus.get_or_none(HandBonus.type**id)
    if (handBonus) == None:
        raise HTTPException(status_code=404, detail="Pitching hand bonus not found.")
    return handBonus


@dataRouter.get(
    "/currentSeason",
    tags=["data"],
)
def get_current_season() -> list[SeasonDefinition]:
    seasons = Season.select().order_by(Season.league).dicts()
    if len(seasons) == 0:
        raise HTTPException(status_code=404, detail="No current season data found.")
    return [*seasons]
