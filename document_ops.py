import docx

def generate_document(content_list, file_path):
    '''Generate a document from content and save it to a specific path'''
    organised_key_list = ['roles_and_responsibilities', 'required_stuff', 'preferred_stuff', 'passed_url']
    document = docx.Document()

    for content in content_list:
        document.add_heading(f"{content['title']} -- {content['company']}", level=4)
        document.add_paragraph(content['introduction'])

        table = document.add_table(rows=2, cols=len(organised_key_list))
        for header_name, header_cell in zip(organised_key_list, table.rows[0].cells):
            header_cell.text = header_name

        ordered_items = [content[key] for key in organised_key_list]
        for item, cell in zip(ordered_items, table.rows[1].cells):
            cell.text = item

        document.add_page_break()

    document.save(file_path)

