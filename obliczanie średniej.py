liczby = []

while True:
    wejscie = input("Podaj liczbę (lub wpisz 'stop', aby zakończyć): ")
    
    if wejscie.lower() == 'stop':
        break
    
    try:
        liczba = float(wejscie)
        liczby.append(liczba)
    except ValueError:
        print("To nie jest poprawna liczba!")

if liczby:
    srednia = sum(liczby) / len(liczby)
    print(f"Średnia z {len(liczby)} liczb wynosi: {round(srednia, 2)}")
else:
    print("Nie podano żadnych liczb.")