print("GRA PRZYGODOWA")
print("Budzisz się na opuszczonej stacji kosmicznej.")

print("\nWidzisz dwa korytarze:")
print("1 - Idź do centrum sterowania")
print("2 - Idź do hangaru")

wybor1 = input("Twój wybór: ")

if wybor1 == "1":

    print("\nJesteś w centrum sterowania.")
    print("1 - Wyślij sygnał ratunkowy")
    print("2 - Sprawdź kamery")

    wybor2 = input("Twój wybór: ")

    if wybor2 == "1":
        print("\nStatek ratunkowy odbiera sygnał.")
        print("WYGRAŁEŚ!")
    else:
        print("\nNa kamerach widzisz potwora który Cię znajduje.")
        print("PRZEGRAŁEŚ!")

elif wybor1 == "2":

    print("\nJesteś w hangarze.")
    print("1 - Uruchom statek")
    print("2 - Poszukaj paliwa")

    wybor2 = input("Twój wybór: ")

    if wybor2 == "1":
        print("\nStatek nie ma paliwa.")
        print("PRZEGRAŁEŚ!")
    else:
        print("\nZnajdujesz paliwo i uciekasz ze stacji.")
        print("WYGRAŁEŚ!")

else:
    print("Niepoprawny wybór.")