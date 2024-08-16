from fastapi import FastAPI

tags_metadata = []

app = FastAPI(
    title="MLR-Reference API",
    summary="The MLR-Reference API allows users to access read-only data from the MLR database.",
    description="For issues, please contact Sterling Turlington on the MLR Main Discord (@veritablequandary).",
    version="1.0.0",
    docs_url="/",
    redoc_url=None,
    openapi_tags=tags_metadata,
)
