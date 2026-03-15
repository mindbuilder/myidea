import random

liczba_do_odgadniecia = random.randint(1, 100)
proby = 0

while True:
    guess = int(input("Zgadnij liczbę (1-100): "))
    proby += 1

    if guess < liczba_do_odgadniecia:
        print("Za mało!")
    elif guess > liczba_do_odgadniecia:
        print("Za dużo!")
    else:
        print(f"Gratulacje! Zgadłeś liczbę {liczba_do_odgadniecia} w {proby} próbach.")
        break