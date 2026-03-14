import json
import os

PLIK = "zadania.json"

# wczytanie zadań
def wczytaj():
    if os.path.exists(PLIK):
        with open(PLIK, "r") as f:
            return json.load(f)
    return []

# zapis zadań
def zapisz(zadania):
    with open(PLIK, "w") as f:
        json.dump(zadania, f, indent=4)

# wyświetlanie
def pokaz(zadania):
    if not zadania:
        print("Brak zadań")
    for i, z in enumerate(zadania):
        status = "✔" if z["done"] else "✘"
        print(f"{i+1}. {z['task']} [{status}]")

# dodawanie
def dodaj(zadania):
    tekst = input("Podaj zadanie: ")
    zadania.append({"task": tekst, "done": False})

# oznaczenie jako wykonane
def wykonane(zadania):
    pokaz(zadania)
    nr = int(input("Numer zadania: ")) - 1
    if 0 <= nr < len(zadania):
        zadania[nr]["done"] = True

# usuwanie
def usun(zadania):
    pokaz(zadania)
    nr = int(input("Numer do usunięcia: ")) - 1
    if 0 <= nr < len(zadania):
        zadania.pop(nr)

def menu():
    zadania = wczytaj()

    while True:
        print("\n--- LISTA ZADAŃ ---")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz jako wykonane")
        print("4. Usuń zadanie")
        print("5. Wyjście")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            pokaz(zadania)
        elif wybor == "2":
            dodaj(zadania)
        elif wybor == "3":
            wykonane(zadania)
        elif wybor == "4":
            usun(zadania)
        elif wybor == "5":
            zapisz(zadania)
            break
        else:
            print("Niepoprawny wybór")

menu()