from click import group

from icm.service.server import service


@group()
def cli():
    pass


cli.add_command(service)


if __name__ == "__main__":
    cli()
