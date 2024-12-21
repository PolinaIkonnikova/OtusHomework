import json
from copy import copy
from csv import DictReader
from itertools import islice
from pathlib import Path
from typing import Iterator


JSON_PATH = Path(__file__).parent / "users.json"
CSV_PATH = Path(__file__).parent / "books.csv"
RESULT_PATH = Path(__file__).parent / "result.json"


def serialize_json_file(path: Path | str) -> dict:
    with open(path, "r") as f:
        return json.loads(f.read())


def csv_file_iterator(path: Path | str) -> Iterator:
    with open(path, "r") as f:
        for row in DictReader(f):
            yield row


def deserialize_json_file(data: list | dict, path: Path | str) -> None:
    with open(path, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_books(iter_data: Iterator, elem_count: int) -> list:
    return list(map(lambda book_info: {
        "title": book_info["Title"],
        "author": book_info["Author"],
        "pages": int(book_info["Pages"]),
        "genre": book_info["Genre"]
    }, islice(iter_data, elem_count)))


def distribute_books(books_file: str | Path, users_file: str | Path,
                     result_path: str | Path = None) -> list | None:
    # принимаем, что всегда books_file имеет расширение .csv, users_file - .json
    common_data = []
    users_data = serialize_json_file(users_file)
    # вычисляем к-во книг и пользователей, чтобы сразу определить, сколько книг отсыпать каждому
    # пользователю за один проход
    users_count = len(users_data)
    # первый вызов итератора для подсчета суммы
    all_books_count = sum([1 for _ in csv_file_iterator(books_file)])
    whole_books_count = all_books_count // users_count
    # happy_users - пользователи, которые получат + 1 книгу сверху
    happy_users = all_books_count % users_count
    # можно вычислять оставшихся юзеров по индексу, но лучше сделать независимый счетчик
    counter = copy(users_count)
    csv_data_iterator = csv_file_iterator(books_file)
    for user in users_data:
        books_count = whole_books_count if counter > happy_users else whole_books_count + 1
        result = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            # второй вызов итератора для извлечения элементов
            "books": get_books(csv_data_iterator, books_count)
        }
        counter -= 1
        common_data.append(result)

    if result_path:
        deserialize_json_file(common_data, result_path)

    return common_data


if __name__ == '__main__':
    res = distribute_books(CSV_PATH, JSON_PATH, RESULT_PATH)
    assert res[0]['books'] != res[1]['books'] != res[2]['books']
