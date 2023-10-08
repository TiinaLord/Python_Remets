import os


def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


csv_books = get_path("Books.csv")
json_users = get_path("users.json")
result_json = get_path("result.json")
