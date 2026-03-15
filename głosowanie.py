wiek = int(input("Ile masz lat? "))
if wiek >= 18:
    print("Możesz brać udział w głosowaniu.")
else:
    print(f"Jesteś za młody/a. Musisz jeszczepoczekać  {18 - wiek} lat.")