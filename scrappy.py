from pprint import pprint

import click

import document_ops
import http_ops
import parsers

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

    parsed_content_list = []
    for url in url_list:
        domain_name = http_ops.get_domain(url)
        content = http_ops.get_page_content(url)
        content_dict = parsers.parse_content(domain_name, content)
        content_dict['passed_url'] = url
        content_dict['company'] = domain_name
        parsed_content_list.append(content_dict)

    document_ops.generate_document(parsed_content_list, document_file_path)


if __name__ == "__main__":
    cli()
