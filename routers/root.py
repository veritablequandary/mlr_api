from fastapi import APIRouter
from typings.hello_response import HelloResponse


root_router = APIRouter(tags=["/"])


# Since health check must be successful before the API becomes active, no failure responses need to be handled
@root_router.get(
    "hello", name="hello", summary="Check API status", response_model=HelloResponse
)
def hello():
    """
    A successful response indicates that the API is active and ready to receive requests.
    """
    return {"message": "Hello there!"}
