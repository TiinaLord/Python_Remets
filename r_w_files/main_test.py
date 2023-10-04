import json
import csv
from test_files import JS0N_Users, Result_json, CSV_Books


def get_users(file_path):
    with open(file_path, 'r') as json_file:
        users = json.loads(json_file.read())
    return users


def get_books(file_path):
    data = []
    with open(file_path, "r") as CSV_reader:
        rows = csv.DictReader(CSV_reader)
        for row in rows:
            data.append(row)
    return data


def distribute_books(data, users):
    for user in users:
        for book in data:
            while len(book) < len(data) // len(users):
                new_user = {"name": user["name"], "gender": user["gender"], "address": user["address"],
                            "age": user["age"]}
                distribution = {"title": book["Title"], "author": book["Author"], "genre": book["Genre"],
                        "pages": book["Pages"]}
                new_user['books'] = [distribution]
                print(new_user)
                return new_user


def write_json(new_user, file_path):
    with open(file_path, "w") as f:
        json.dump(new_user, f, indent=4)


def main():
    users_file_path = JS0N_Users
    books_file_path = CSV_Books
    users = get_users(users_file_path)
    books = get_books(books_file_path)
    distribution = distribute_books(books, users)
    result_json_file_path = Result_json
    write_json(distribution, result_json_file_path)


if __name__ == "__main__":
    main()
