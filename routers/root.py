from fastapi import APIRouter
from models.hello import HelloResponse


root_router = APIRouter(tags=["/"])


# Since health check must be successful before the API becomes active, no failure responses need to be handled
@root_router.get(
    "hello", name="hello", summary="Check API status", response_model=HelloResponse
)
def hello():
    """
    Use this endpoint to check whether the API is active.
    A JSON response with status code 200 indicates that the API is ready to accept queries.
    """
    return {"message": "Hello there!"}
