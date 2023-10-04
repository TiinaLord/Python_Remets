import os


def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


CSV_Books = get_path("Books.csv")
JS0N_Users = get_path("users.json")
Result_json = get_path("result.json")
