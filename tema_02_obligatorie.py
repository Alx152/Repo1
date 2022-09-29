"""
Exercitiul nr.1
Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else

IF in engleza insemana daca, este un "flow control", respectiv cu ajutorul lui controlam pe unde
merge codul
un IF simplu este ca o usa:
- daca usa este deschisa, respectiv daca conditia este True, se va ecxecuta codul din spatele usii;
- daca usa este inchisa, respectiv daca conditia este False, atunci se trece mai departe, nu se executa
 codul care este in spatele usii, Phyton nu vede in spatele usii inchise
 ELSE in engleza insemana altfel
"""


"""  
Exercitiul nr.2
Verifică și afișează dacă x este număr natural sau nu.
NUMERE NATURALE= sunt numerele întregi strict pozitive (1, 2, 3, …). 0 este primul număr natural.
"""
x = int(input("Introduceti un numar intreg:\n"))
if x >= 0:
    print(f"Numarul introdus este un numar natural.")
else:
    print(f"Numarul introdus NU este un numar natural! Te rog sa introduci un alt numar.")


"""
Exercitiul nr.3
Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
NUMARUL NETRU = 0 ptr adunare/scadere si 1 ptr. inmultire/impartire
"""
x = int(input("Introduceti un numar intreg:\n"))
if x > 2:
    print("Numarul introdus este un numar pozitiv.")
elif x == 0 or x == 1:
        print("Numarul introdus este un numar neutru.")
else:
    print("Numarul introdus este un numar negativ")


"""
Exercitiul nr.4
Verifică și afișează dacă x este intre -2 si 13.
"""
x = int(input("Introduceti un numar intreg intre -2 si 13:\n"))
if -2 <= x <=13:
    print(f"Numarul introdus este {x} si se regaseste in intervalul solicitat -2 si 13")
else:
    print("Numarul introdus NU se regaseste in intervalul solicitat -2 si 13."
          "Te rog sa introduci alt numar!")


"""
Exercitiul nr.5
Verifică și afișează dacă diferenta dintre x si y este mai mica de 5.
"""

xy = input("Introduceti doua numere despartite de spatiu:\n")
x, y = xy.split()
x, y = int(x), int(y)
diferenta = x-y
if diferenta < 5 :
    print(f"Diferenta dintre {x} si {y} este {diferenta} si este mai mica decat 5.")
else:
    print(f"Diferenta dintre {x} si {y}este {diferenta} si NU este mai mica decat 5.")


"""
Exercitiul nr.6
Verifica daca x NU este intre 5 si 27 - a se folosi 'not'
"""

x = int(input("Introduceti un numar intreg intre 5 si 27:\n"))
if not (5<= x >=27) :
    print(f"Numarul {x} se afla in intervalul 5 si 27.")
else:
    print(f"Numarul {x} NU se afla in intervalul 5 si 27.")


"""
Exercitiul nr.7
x si y (int)
Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare.
"""

numere = input("Introduceti doua numere despartite de spatiu:\n")
x, y = numere.split()
x, y = int(x), int(y)
if x == y:
    print (f"Numerele introduse sunt egale")
elif x > y:
    print(f"Numarul {x} este mai mare decat {y}")
else:
    print(f"Numarul {y} este mai mare decat {x}")


"""
Exercitiul nr.8
X,y,z - laturile unui triunghi.
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
"""
Xyz= input("Introduceti trei numere despartite de spatiu:\n")
X, y, z = Xyz.split()
X, y, z = int(X), int(y), int(z)
if X==y and X!=z or y==z and y!=X or z==X and y!=z:
    print("Triunghiul este isoscel.")
elif X==y==z:
    print("Triunghiul este echilateral.")
else:
    print("Triunghiul este oarecare.")


"""
Exercitiul nr.9
Citeste o litera de la tastatura.
Verifica si afiseaza daca este volaca sau nu.
"""

x = input("Introduceti o litera de la tastutura:\n")
if x=="a" or x=="e" or x=="i" or x=="o"or x=="u" or x=="ă":
    print("Litera introdusa este o vocala.")
else:
    print("Litera introdusa este o consoana.")


"""
Transforma si printeaza notele din sistemul romanesc in >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
"""

nota = int(input("Introduceti nota de la examen:\n"))
if 1 <= nota <= 4 :
    print("Ai luat calificativul F")
elif 4 < nota <= 6:
    print("Ai luat calificativul E")
elif 6 < nota <= 7:
    print("Ai luat calificativul D")
elif 7 < nota <= 8:
    print("Ai luat calificativul C")
elif 8 < nota <= 9:
    print("Ai luat calificativul B")
elif 9 < nota <= 10:
    print("Ai luat calificativul A")
else:
    print("Nota nu se regaseste in sistemul romanesc! Introduceti nota corecta!")



