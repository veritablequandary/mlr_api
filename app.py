from fastapi import FastAPI
from open_api_tags import tags_metadata
from routers.root import root_router

app = FastAPI(
    title="MLR-Reference API",
    summary="The MLR-Reference API allows users to access read-only data from the MLR database.",
    description="For issues, please contact Sterling Turlington on the MLR Main Discord (@veritablequandary).",
    version="1.0.0",
    docs_url="/",
    redoc_url="/redoc",
    openapi_tags=tags_metadata,
)


app.include_router(root_router)
