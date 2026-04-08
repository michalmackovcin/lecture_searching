from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name


def main():
    pass


def read_data(file_name, pole):
    # povolené klúče
    povolene = ["unordered_numbers", "ordered_numbers", "dna_sequence"]

    # kontrola klúča
    if pole not in povolene:
        return None

    # cesta k súboru
    file_path = Path.cwd() / file_name

    # načítanie JSON suboru
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # vrátenie dat podla klúču
    return data[pole]

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)


if __name__ == "__main__":
    main()

def linear_search(file_name, pole):


