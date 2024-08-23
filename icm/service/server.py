from click import option, group, IntRange

from icm.utilities.utils import get_logger

logger = get_logger(__name__)


@group()
def service():
    pass


@service.command()
@option("--host", default="0.0.0.0", type=str, show_default=True)
@option(
    "--port",
    default="8080",
    type=IntRange(0, 65536),
    show_default=True,
    help="Server port number",
)
@option(
    "--model",
    default="model_path",
    type=str,
    show_default=True,
    help="Path to model directory or file.",
)
def run_server(host, port, model):
    import uvicorn
    from icm.service.factories import (
        create_app,
    )

    app = create_app()
    logger.info(f"Loading model from {model}")
    app.state.model.load(model)

    logger.info(f"Starting server on port {port}")
    uvicorn.run(app, host=host, port=port, timeout_keep_alive=0)
