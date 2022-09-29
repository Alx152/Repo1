# Exercitiul nr.1

"""
o variabila reprezinta o zona din memoria unui calculator care contine diferite tipuri de date
o variabila reprezinta un container din memorie care stocheaza valori
"""

# Exercitiul nr.2
# declarare si initializare o variabila de tip string
serie_motor = 'A165J138'
print(serie_motor)

# declarare si initializare o variabila de tip integer (int)
capacitatea_motorului = 1598
print(capacitatea_motorului)

# declarare si initializare o variabila de tip float
pret_vanzare = 10050.789
print(pret_vanzare)

# declarare si initializare o variabila de tip boolean (bool)
norma_poluare = True
print(norma_poluare)
print("============================================================")

# Exercitiul nr.3
# verific tipul de date din variabila string
print(type(serie_motor))

# verific tipul de date din variabila integer
print(type(capacitatea_motorului))

# verific tipul de date din variabila float
print(type(pret_vanzare))

# verific tipul de date din variabila boolean
print(type(norma_poluare))
print("============================================================")

# Exercitiul nr.4
# folosesc functia round pentru a rotunji "float"-ul si suprascriu aceasta variabila
pret_vanzare = round(pret_vanzare, 0)   # daca il sterg pe 0 dintre paranteze, variabila devine de tip 'int'
print(pret_vanzare)

# verific tipul de date din variabila float
print(type(pret_vanzare))
print("============================================================")

# Exercitiul nr.5
print(f"Autoturismul are seria de motor: {serie_motor}.")
print(f"Autoturismul are capacitatea cilindrica de: {capacitatea_motorului} cm3.")
print(f"Pretul de vanzare al autoturismului este de: {pret_vanzare} euro.")
print(f"Autoturismul are norma de poluare euro 5: {norma_poluare}")
print("============================================================")

# Exercitiul nr.6
numele = input("Introdu numele:")
prenumele = input("Introdu prenumele:")
numele_complet = numele + " " + prenumele
print(f"Numele complet este {numele_complet}")
total_caractere = len(numele_complet)
print(f"Numele complet are {total_caractere} caractere.")
print("============================================================")

# Exercitiul nr.7
lungimea = int(input("Introdu lungimea dreptunghiului: "))
latimea = int(input("Introdu latimea dreptunghiului: "))
aria_dreptunghiului = (lungimea) * (latimea)
print(f"Aria dreptunghiului este {aria_dreptunghiului}.")
print("============================================================")

# Exercitiul nr.8
text_dat = "Coral is either the stupidest animal or the smartest rock"
cuvantul_the= text_dat.count(" the ") # daca nu pui spatiu in ghilimele numara si in interiorul cuvintelor
print(cuvantul_the)
print("============================================================")

# Exercitiul nr.9
text_dat = "Coral is either the stupidest animal or the smartest rock"
cuvantul_the= text_dat.count(" the ")
print(f"Cuvantul 'the' apare de {cuvantul_the} ori.")
print("============================================================")

# Exercitiul nr.10
text_dat = input("Coral is either the stupidest animal or the smartest rock")
print(text_dat.split(' '))
assert text_dat.isdigit(), f"{text_dat} NU contine doar numere!"






