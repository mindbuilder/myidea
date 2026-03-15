tekst = input("Podaj tekst: ")
odwrocony_tekst = ""
i = len(tekst) - 1

while i >= 0:
    odwrocony_tekst += tekst[i]
    i -= 1

print("Odwrócony tekst:", odwrocony_tekst)