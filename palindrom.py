tekst = input("Podaj słowo lub zdanie: ").replace(" ", "").lower()
if tekst == tekst[::-1]:
    print("To jest palindrom!")
else:
    print("To nie jest palindrom.")
