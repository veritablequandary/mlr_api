from fastapi import FastAPI

app = FastAPI(
    title="MLR-Reference API",
    summary="The MLR-Reference API allows users to access read-only data from the MLR database.",
    description="For issues, please contact Sterling Turlington on the MLR Main Discord (@veritablequandary).",
    version="0.1.0",
    docs_url=None,
    redoc_url="/",
)
