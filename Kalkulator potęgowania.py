def poteguj(podstawa, wykladnik):
    return podstawa ** wykladnik

p = float(input("Podaj podstawę: "))
w = float(input("Podaj wykładnik: "))
print(f"Wynik: {poteguj(p, w)}")
