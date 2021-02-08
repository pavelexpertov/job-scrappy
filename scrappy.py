import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('job_url')
def get_metadata(job_url):
    '''Get metadata from a single URL source'''
    print(job_url)

@cli.command()
@click.argument('urls_file_path')
@click.argument('document_file_path')
def get_metadatas(urls_file_path, document_file_path):
    '''Save parsed job metadata that's described in a file to a specific document'''
    with open(urls_file_path) as file_obj:
        url_list = [line.strip() for line in file_obj.readlines()]

    click.echo(url_list)

if __name__ == "__main__":
    cli()
