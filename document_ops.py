import docx

def generate_document(content_list, file_path):
    '''Generate a document from content and save it to a specific path'''
    organised_key_list = ['title', 'introduction', 'roles_and_responsibilities', 'required_stuff', 'preferred_stuff', 'company', 'passed_url']
    document = docx.Document()
    table = document.add_table(rows=len(content_list)+1, cols=len(organised_key_list))
    for header_cell, header_name in zip(table.rows[0].cells, organised_key_list):
        header_cell.text = header_name

    for content_dict, row in zip(content_list, table.rows[1:]):
        ordered_items = [content_dict[key] for key in organised_key_list]
        for item, cell in zip(ordered_items, row.cells):
            cell.text = item

    document.save(file_path)

