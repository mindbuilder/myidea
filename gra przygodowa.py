import time

def pauza():
    time.sleep(1)

def epizod1():
    print("\nEPIZOD 1 - Tajemniczy las")
    print("Idziesz przez ciemny las. Dochodzisz do rozwidlenia dróg.")
    print("1 - Idź w lewo (ciemna ścieżka)")
    print("2 - Idź w prawo (oświetlona ścieżka)")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        epizod2_las()
    elif wybor == "2":
        epizod2_wioska()
    else:
        print("Niepoprawny wybór.")
        epizod1()

def epizod2_las():
    print("\nEPIZOD 2 - Spotkanie z wilkiem")
    print("Na ścieżce pojawia się wilk.")
    print("1 - Uciekaj")
    print("2 - Spróbuj go oswoić")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        print("\nUciekasz i wpadasz do starej chaty.")
        epizod3_chata()
    elif wybor == "2":
        print("\nWilk okazuje się przyjazny i prowadzi Cię do skarbu.")
        koniec_dobry()
    else:
        print("Niepoprawny wybór.")
        epizod2_las()

def epizod2_wioska():
    print("\nEPIZOD 2 - Opuszczona wioska")
    print("Docierasz do starej wioski.")
    print("1 - Wejdź do największego domu")
    print("2 - Poszukaj czegoś na ulicy")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        epizod3_dom()
    elif wybor == "2":
        print("\nZnajdujesz stary klucz.")
        epizod3_skrzynia()
    else:
        print("Niepoprawny wybór.")
        epizod2_wioska()

def epizod3_chata():
    print("\nEPIZOD 3 - Stara chata")
    print("W chacie znajduje się skrzynia.")
    print("1 - Otwórz skrzynię")
    print("2 - Wyjdź z chaty")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        koniec_zly()
    elif wybor == "2":
        koniec_dobry()
    else:
        print("Niepoprawny wybór.")
        epizod3_chata()

def epizod3_dom():
    print("\nW domu spotykasz ducha.")
    print("1 - Rozmawiaj z nim")
    print("2 - Uciekaj")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        koniec_dobry()
    elif wybor == "2":
        koniec_zly()
    else:
        print("Niepoprawny wybór.")
        epizod3_dom()

def epizod3_skrzynia():
    print("\nNa środku wioski jest zamknięta skrzynia.")
    print("1 - Spróbuj ją otworzyć")
    print("2 - Zostaw ją i odejdź")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        koniec_dobry()
    elif wybor == "2":
        koniec_zly()
    else:
        print("Niepoprawny wybór.")
        epizod3_skrzynia()

def koniec_dobry():
    print("\n*** ZNALAZŁEŚ SKARB I WYGRAŁEŚ! ***")

def koniec_zly():
    print("\n*** WPUŚCIŁEŚ SIĘ W PUŁAPKĘ. KONIEC GRY. ***")

def start():
    print("================================")
    print("      GRA PRZYGODOWA")
    print("================================")
    print("Wpisuj numer opcji i naciśnij ENTER.")
    pauza()
    epizod1()

start()