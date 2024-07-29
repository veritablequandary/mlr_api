from fastapi import APIRouter, HTTPException
from models import *

####################
# /games router
####################

dataRouter = APIRouter(
    prefix="/games",
    tags=["games"],
    responses={
        404: {"description": "The requested resource was not found."},
        500: {"description": "Internal server error."},
    },
)

####################
# /games/inProgress
####################


@dataRouter.get(
    "/inProgress/{league}",
    tags=["games"],
    description="Data on all in-progress games in the specified league.",
    response_description="A list of data on all in-progress games from the specified league.",
)
def get_in_progress(league: str) -> list[GameTypeDefinition]:
    games = (
        Game.select()
        .where((Game.complete != 1) & (str.lower(Game.league) == league.lower()))
        .order_by(Game.gameID)
        .dicts()
    )

    if len(games) == 0:
        raise HTTPException(
            status_code=404,
            detail="No in-progress games found for the specified league.",
        )
    return [*games]


####################
# /games/scoreboard
####################


@dataRouter.get(
    "/scoreboard/{league}",
    tags=["games"],
    description="Data on all current-session games in the specified league.",
    response_description="A list of data on all current-session games from the specified league.",
)
def get_scoreboard(league: str) -> list[GameTypeDefinition]:
    currentSeason = Season.get_by_id("mlr")

    games = (
        Game.select()
        .where(
            (Game.season == currentSeason.season)
            & (Game.session == currentSeason.session)
            & (str.lower(Game.league) == league.lower())
        )
        .order_by(Game.gameID)
        .dicts()
    )

    if len(games) == 0:
        raise HTTPException(
            status_code=404,
            detail="No current-session games found for the specified league.",
        )
    return [*games]
