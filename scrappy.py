import click

@click.group()
def cli():
    pass

@click.command()
def generate_document():
    print('hey man')

cli.add_command(generate_document)

if __name__ == "__main__":
    cli()
