# Ex_1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# Afisare
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)    # output : ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

# Inversează ordinea folosind slicing
print(note_muzicale[: :-1])     # output : ['do', 'si', 'la', 'sol', 'fa', 'mi', 're', 'do']

# suprascrie această listă  si printează varianta actuală (inversată)
note_inversate = note_muzicale[: : -1]
print(note_inversate)    # output : ['do', 'si', 'la', 'sol', 'fa', 'mi', 're', 'do']

# Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
# Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
note_inversate.reverse()     # output: ['do', 'si', 'la', 'sol', 'fa', 'mi', 're', 'do']

# Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
print(note_inversate)    # output: ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']


"""
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să suprascrii lista sau să o salvezi într-o listă nouă. 
Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. 
Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment.
"""

# Ex_2. De câte ori apare ‘do’?
print(note_muzicale.count('do'))    # output : 2

# Ex_3. Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista1.append(lista2)   #  adauga un element la final ; lista2 a adaugat-o ca un singur string
print(lista1)                 # output : [3, 1, 0, 2, [6, 5, 4]]

# varianta 2
lista1.remove(lista2)   # am adus lista 1 la valoarea initiala
print(lista1)                # output: [3, 1, 0, 2]
lista1.extend(lista2)   # adauga mai multe elemente la final; lista2 a adaugat-o ca mai multe stringuri
print(lista1)               # output : [3, 1, 0, 2, 6, 5, 4]

# Ex_4. Sortează și afișază lista generată la exercițiul anterior
lista1.sort()
print(lista1)       # output: [0, 1, 2, 3, 4, 5, 6]

#
#
# Sterge numărul 0 folosind o funcție.
# Afișaza iar lista.

lista1.remove(0)
print(lista1)       # output: [1, 2, 3, 4, 5, 6]

# Ex_5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.

if lista1 != [1, 2, 3, 4, 5, 6]:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')   # output : Lista nu este goala.

# Ex_6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lista1.clear()
print(lista1)       # output : []

# Ex_7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.

if lista1 != [1, 2, 3, 4, 5, 6]:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')       # output : Lista este goala.

# Ex_8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())     # output : dict_keys(['Ana', 'Gigel', 'Dorel'])

# Ex_9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
#print(dict1['Ana'])                             # output : 8
print(f"Ana a luat nota {dict1['Ana']}.")       # output : Ana a luat nota 8.
print(f"Gigel a luat nota {dict1['Gigel']}.")   # output : Gigel a luat nota 10.
print(f"Dorel a luat nota {dict1['Dorel']}.")   # output : Dorel a luat nota 5.

# Ex_10. Dorel a făcut contestație și a primit 6
# Modifică nota lui Dorel în 6
dict1['Dorel'] = 6

# Printează nota după modificare
print(f"Dorel a luat nota {dict1['Dorel']}.")   # output : Dorel a luat nota 6.

# Ex_11. Gigel se transferă din clasă
# Căuta o funcție care să îl șteargă
del dict1['Gigel']
print(dict1)        # output :  {'Ana': 8, 'Dorel': 6}

# Vine un coleg nou. Adaugă Ionică, cu nota 9
dict1 ['Ionica'] = 9

# Printează noii elevi
print(dict1)        # output :  {'Ana': 8, 'Dorel': 6, 'Ionica': 9}

# Ex_12. Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
#print(type(weekend))        # output : <class 'set'>
# Adaugă în zilele_sapt ‘luni’
# Afișeaza zile_sapt
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
zile_sapt.add('luni')   # nu se adauga 'luni' deoarece exista deja
print(zile_sapt)        # output {'sâmbăta', 'luni', 'marți', 'miercuri', 'duminică', 'joi', 'vineri'}

# Ex_13. Folosește un if și verifică dacă:
# Weekend este un subset al zilelor din săptămânii.
# Weekend nu este un subset al zilelor din săptămânii.
weekend = {'sâmbăta', 'duminică'}         # output : <class 'set'>

if weekend <= zile_sapt:
    print("Weekend este un subset al zilelor saptamanii")
else:
    print("Weekend NU este un subset al zilelor saptamanii")    # output : Weekend este un subset al zilelor saptamanii

# Weekend nu este un subset al zilelor din săptămânii.
if weekend in zile_sapt:
    print("Weekend este un subset al zilelor saptamanii")
else:
    print("Weekend NU este un subset al zilelor saptamanii")  # output : Weekend NU este un subset al zilelor saptamanii

# Ex_14. Afișează diferențele dintre aceste 2 seturi.
set_diferente = zile_sapt.difference(weekend)
print(set_diferente)                                    # output : {'marți', 'miercuri', 'joi', 'luni', 'vineri'}

# 15. Afișază intersecția elementelor din aceste 2 seturi.
set_intersectii = zile_sapt.intersection(weekend)
print (set_intersectii)                                 # output : {'duminică', 'sâmbăta'}