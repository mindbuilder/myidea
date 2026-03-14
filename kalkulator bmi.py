waga = float(input("Podaj swoją wagę w kg:"))
wzrost = float(input("Podaj swój wzrost w metrach (np. 1.75): "))

bmi = waga / (wzrost ** 2)

print("Twoje BMI wynosi:", round(bmi, 2))

if bmi < 18.5:
    print("Niedowaga")
elif bmi < 25:
    print("Waga prawidłowa")
elif bmi < 30:
    print("Nadwaga")
else:
    print("Otyłość")
    