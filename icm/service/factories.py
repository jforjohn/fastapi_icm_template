from os import environ
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import make_asgi_app

from icm.model.intent_classifier import IntentClassifier


def create_app() -> FastAPI:
    """
    Factory function to create a FastAPI application and register the project's routes
    :return: the FastAPI application
    """

    enable_docs = bool(environ.get("SHOW_DOCS", True))

    docs_args = {}
    if enable_docs is False:
        docs_args = {"docs_url": None, "redoc_url": None}
    api = FastAPI(**docs_args)
    Instrumentator().instrument(api, metric_namespace="model_service")
    # Add prometheus asgi middleware to route /metrics requests
    metrics_app = make_asgi_app()
    api.mount("/metrics", metrics_app)

    api.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["DELETE", "GET", "POST", "PUT"],
        allow_headers=["*"],
    )
    model = IntentClassifier()

    register_routers(api)
    api.state.model = model  # Store the model in the FastAPI application state

    return api


def register_routers(api: FastAPI):
    """
    Registers the project's routes to the FastAPI application
    :param api: the FastAPI application on which to register the routes
    """
    from icm.service.routes import health_router
    from icm.service.routes import model_router

    api.include_router(health_router)
    api.include_router(model_router)
