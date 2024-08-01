from fastapi import APIRouter, HTTPException
from models.game import *
from models.season import *

gamesRouter = APIRouter(
    prefix="/games",
    tags=["games"],
)


@gamesRouter.get(
    "/inProgress/{league}",
    tags=["games"],
)
def get_in_progress(league: str) -> list[GameDefinition]:
    games = (
        Game.select()
        .where((Game.complete != 1) & (Game.league**league))
        .order_by(Game.gameID)
        .dicts()
    )

    if len(games) == 0:
        raise HTTPException(
            status_code=404,
            detail="No in-progress games found for the specified league.",
        )
    return [*games]


@gamesRouter.get(
    "/scoreboard/{league}",
    tags=["games"],
)
def get_scoreboard(league: str) -> list[GameDefinition]:
    currentSeason = Season.get_by_id("mlr")

    games = (
        Game.select()
        .where(
            (Game.season == currentSeason.season)
            & (Game.session == currentSeason.session)
            & (Game.league**league)
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
