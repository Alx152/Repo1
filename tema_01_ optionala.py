# Exercitiul nr.1 (incomplet )
sir1 = input("Introduceti un strig impar: ")
sir_impar = len(sir1) % 2 != 0
if len(sir1) % 2 != 0 == True:
    print("Sirul introdus este impar")
else:
    print("Sirul introdus NU este impar. Introduceti alt sir.")
print("================================================")

# Exercitiul nr.2
# un palindrom nu este altceva decat un numar sau un sir de caractere care ramane nealterat atunci cand este inversat
def is_palindrome(text):
    string = text
    if (string==string [::-1]):
        print("este palindorm")
        return True
    else:
        print("nu este palindrom")
        return False
assert is_palindrome("noon")
assert is_palindrome("12321")
#assert is_palindrome("baba")  # l-am comentat deoarece da eroare, nefiind palindrom
print("================================================")

# Exercitul nr.3 (nu am stiut)
# print(input(f'alabala portocala' + {a==alabala} + {b==portocala}))
# sir1, sir2 = input("alabala portocalaa").split(' ')  # introduceti alabala portocala
# print(sir1, sir2)
print("================================================")

# Exercitiul nr.4 (copiat de pe disord)
text1 = input("Introduceti un text de la tastatura: ")
first_char = text1[0]  # ne va da prima litera
last_index = int(text1.rindex(first_char))  # asa aflam indexul unde gasim prima litera ultima oara in string de la stanga la dreapta
rest_chars = text1[last_index:len(text1)]  # asa putem face sa printam doar anumite caractere din string dintr-un interval(index)
# important print(string[2:5]) va printa doar caracterele de la index 2 pana la 4 nu si pe cel de la index 5
text1 = text1[1:last_index].replace(first_char, first_char.upper())  # asa schimbam prima litera in upper in afara de prima aparitie si ultima
text_cu_upper = first_char + text1 + rest_chars
print(text_cu_upper)  # printam ce o iesit
print("================================================")

# Exercitiul nr.5
user = input("Introduceti userul: ")
parola = input("Introduceti parola: ")
lungime_parola = str(len(parola))
print(f"Parola pentru user {user} este {parola} si are {lungime_parola} caractere.")
print("================================================")
