from fastapi import APIRouter


root_router = APIRouter(tags=["/"])


# Since health check must be successful before the API becomes active, no failure responses need to be handled
@root_router.get("/hello", summary="Check API status")
def hello():
    """
    Use this endpoint to check whether the API is active.
    A JSON response with status code 200 indicates that the API is ready to accept queries.
    """
    return {"message": "Hello there!"}
