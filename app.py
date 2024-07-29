from fastapi import FastAPI
from routers.data import dataRouter
from routers.games import gamesRouter

####################
# Tag definitions (docs)
####################

tag_definitions = [
    {
        "name": "calculators",
        "description": "Calculate ranges and AB results for pitcher/batter matchups.",
    },
    {
        "name": "data",
        "description": "Information related to rules, game mechanics, etc.",
    },
    {
        "name": "games",
        "description": "Information about current and past games and plate appearances.",
    },
    {
        "name": "players",
        "description": "Information about players, player performances, and statistics",
    },
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
# Add routers to API instance
####################

app.include_router(dataRouter)
app.include_router(gamesRouter)
