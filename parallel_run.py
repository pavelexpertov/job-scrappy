import concurrent.futures
import subprocess

def worker_function(text_file_name):
    '''A function used by a worker thread for working with specific arguments'''
    document_name = text_file_name[:-4].replace('_', ' ').title() + ".docx"
    command = f"pipenv run python ./scrappy.py get-metadatas {text_file_name} '{document_name}'"
    process = subprocess.check_output(command, shell=True)

if __name__ == "__main__":
    file_txt_list = [
        'data_engineer.txt',
        'data_scientist_lead.txt',
        'data_scientist.txt',
        'machine_learning_engineer.txt',
        'postdoctoral_researcher.txt',
        'research_analyst.txt',
        'research_engineer.txt',
        'research_scientist.txt',
        'software_engineer.txt'
    ]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures_list = []
        for file_name in file_txt_list:
            future = executor.submit(worker_function, file_name)
            futures_list.append(future)
        fs_tuples = concurrent.futures.wait(futures_list)
        print(fs_tuples)
