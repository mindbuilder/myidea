masa = float(input("Podaj swoją masę ciała w kg:"))
wzrost = float(input("Podaj swój wzrost w metrach (np. 1.75): "))

bmi = masa / (wzrost ** 2)

print("Twoje BMI wynosi:", round(bmi, 3))

if bmi < 18.5:
    print("Masz niedowagę")
elif bmi < 25:
    print("Twoja waga jest w normie")
elif bmi < 30:
    print("Masz nadwagę")
else:
    print("Masz otyłość")


    