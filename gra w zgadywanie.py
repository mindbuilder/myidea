import random

liczba_do_zgadniecia = random.randint(1, 100)
proby = 0

while True:
    zgadywana_liczba = int(input("Zgadnij liczbę (od 1 do 100): "))
    proby += 1

    if zgadywana_liczba == liczba_do_zgadniecia:
        print(f"Brawo! Zgadłeś liczbę {liczba_do_zgadniecia} w {proby} próbach.")
        break
    elif zgadywana_liczba < liczba_do_zgadniecia:
        print("Liczba jest większa.")
    else:
        print("Liczba jest mniejsza.")