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

def linear_search(zoznam, hladane):
    pozícia= []
    počet= 0
    i= 0
    while i < len(zoznam):
        if zoznam[i]==hladane:
            pozícia.append(i)
            počet +=1
        i +=1
    return {
        "positions":pozícia,
        "count":počet
    }
def main():
    # načítanie dát zo súboru
    sequential_data = read_data("sequential.json", "unordered_numbers")

    hladane_cislo = 5
    vysledok = linear_search(sequential_data, hladane_cislo)

    print("Pozícia hľadaného čísla:", vysledok["positions"])
    print("Počet výskytov:", vysledok["count"])
if __name__ == "__main__":
    main()

def binary_search(list,chcené):
    lavy=0
    pravy=len(list)
    while lavy <= pravy:
        stred=(lavy+pravy)//2

        if list[stred]==chcené:
            return stred
        elif list[stred] < chcené:
            lavy=stred+1
        else:
            pravy=stred-1
    return None
def main():
    # načítanie zoradeného zoznamu zo súboru
    ordered_data = read_data("sequential.json", "ordered_numbers")

    # číslo, ktoré chceme nájsť
    hladane_cislo = 70

    # zavolanie binárneho vyhľadávania
    index = binary_search(ordered_data, hladane_cislo)

    # výpis výsledku
    if index is not None:
        print(f"Hľadané číslo {hladane_cislo} je na indexe: {index}")
    else:
        print(f"Hľadané číslo {hladane_cislo} sa v zozname nenachádza.")

# spustenie programu
if __name__ == "__main__":
    main()







