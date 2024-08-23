from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from prometheus_client import Histogram

from icm.model.intent_classifier import IntentClassifier


model_router = APIRouter(tags=["model"])
health_router = APIRouter(tags=["health"])

model = IntentClassifier()

request_length_counter = Histogram(
    "number_of_input_chars_histogram",
    "number of input chars in the request",
    buckets=[0, 1, 10, 100, 1000, 2000],
    labelnames=["endpoint"],
)


@health_router.get("/ready", tags=["health"])
def ready(request: Request) -> JSONResponse:
    """
    Check if the model is ready.

    Returns:
        A JSON response indicating status.
    """
    model: IntentClassifier = request.app.state.model

    if model.is_ready():
        return JSONResponse(content={"status": "OK"})
    else:
        raise HTTPException(status_code=423, detail="Not ready")


@model_router.post("/intent", response_model=str)
def intent(query: str, request: Request) -> JSONResponse:
    """
    Endpoint for classifying the intent of a text message.
    Request body should be a json object with a single key 'text' containing the text message to classify.
    Response will be a json object with a single key 'intents' containing a list of labels.
    """
    request_length_counter.labels(
        endpoint="intent",
    ).observe(len(query))
    # Implement this function according to the given API documentation
    model: IntentClassifier = request.app.state.model
    return JSONResponse(content={"intents": ["intent1", "intent2"]})
