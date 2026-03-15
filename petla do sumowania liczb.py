num = int(input("Podaj liczbę: "))
suma = 0

for i in range(1, num + 1):
    suma += i

print("Suma liczb od 1 do", num, "to:", suma)