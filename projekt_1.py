"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tereza Čachotská
email: tera.cachotska@gmail.com
discord: Terka Č.#6582
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
cara = "-" * 40
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
delka_slov = {}
vycistena_slova = []
users = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
}
username = input("username: ") 
password = input("password: ")
print(cara)
if users.get(username) == password:
    print("Welcome to the app, ", username, 
    "\nWe have 3 texts to be analyzed.")
    print(cara)
else:
    print("unregistered user, terminating the program..")
    quit()
vyber = input("Enter a number btw. 1 and 3 to select: ")
print(cara)
if vyber == "1":
    for slova in TEXTS[0].split():
        count1 += 1
    print("There are", count1, "words in the selected text.")
    for zac_velke in TEXTS[0].split():
        if (zac_velke.istitle()):
            count2 += 1
    print("There are", count2, "titlecase word.")
    for cele_velke in TEXTS[0].split():
        if cele_velke.isupper():
            count3 += 1
    print("There are", count3, "uppercase words.") 
    for male in TEXTS[0].split():
        if male.islower():
            count4 += 1
    print("There are", count4, "lowercase words.")
    for cisla in TEXTS[0].split():
        if cisla.isdigit():
            count5 += 1
    print("There are", count5, "numeric strings.")
    for cislo in TEXTS[0].split():
        if cislo.isdigit():
            count6 += int(cislo)
    print("The sum of all the numbers", count6)
    print(cara)
    print("LEN|    OCCURENCES    |NR.")
    print(cara)
    for slovo in TEXTS[0].split():
        vycistena_slova.append(slovo.strip(",.:;").lower())
    for slova in vycistena_slova:
        length = len(slova)
        if length in delka_slov:
            delka_slov[length] += 1
        else:
            delka_slov[length] = 1
    sorted_delka_slov = sorted(delka_slov.items(), key=lambda x: x[0])
    for length, count in sorted_delka_slov:
        if length < 10:
            print(f"{'  '}{length}|{'*' * count}{' ' * (18 - count)}|{count}")    
        else: 
            print(f"{' '}{length}|{'*' * count}{' ' * (18 - count)}|{count}")    
elif vyber == "2":
    for slova in TEXTS[1].split():
        count1 += 1
    print("There are", count1, "words in the selected text.")
    for zac_velke in TEXTS[1].split():
        if (zac_velke.istitle()):
            count2 += 1
    print("There are", count2, "titlecase word.")
    for cele_velke in TEXTS[1].split():
        if cele_velke.isupper():
            count3 += 1
    print("There are", count3, "uppercase words.") 
    for male in TEXTS[1].split():
        if male.islower():
            count4 += 1
    print("There are", count4, "lowercase words.")
    for cisla in TEXTS[1].split():
        if cisla.isdigit():
            count5 += 1
    print("There are", count5, "numeric strings.")
    for cislo in TEXTS[1].split():
        if cislo.isdigit():
            count6 += int(cislo)
    print("The sum of all the numbers", count6)
    print(cara)
    print("LEN|    OCCURENCES    |NR.")
    print(cara)
    for slovo in TEXTS[1].split():
        vycistena_slova.append(slovo.strip(",.:;").lower())
    for slova in vycistena_slova:
        length = len(slova)
        if length in delka_slov:
            delka_slov[length] += 1
        else:
            delka_slov[length] = 1
    sorted_delka_slov = sorted(delka_slov.items(), key=lambda x: x[0])
    for length, count in sorted_delka_slov:
        if length < 10:
            print(f"{'  '}{length}|{'*' * count}{' ' * (18 - count)}|{count}")    
        else: 
            print(f"{' '}{length}|{'*' * count}{' ' * (18 - count)}|{count}")
elif vyber == "3":
    for slova in TEXTS[2].split():
        count1 += 1
    print("There are", count1, "words in the selected text.")
    for zac_velke in TEXTS[2].split():
        if (zac_velke.istitle()):
            count2 += 1
    print("There are", count2, "titlecase word.")
    for cele_velke in TEXTS[2].split():
        if cele_velke.isupper():
            count3 += 1
    print("There are", count3, "uppercase words.") 
    for male in TEXTS[2].split():
        if male.islower():
            count4 += 1
    print("There are", count4, "lowercase words.")
    for cisla in TEXTS[2].split():
        if cisla.isdigit():
            count5 += 1
    print("There are", count5, "numeric strings.")
    for cislo in TEXTS[2].split():
        if cislo.isdigit():
            count6 += int(cislo)
    print("The sum of all the numbers", count6)
    print(cara)
    print("LEN|    OCCURENCES    |NR.")
    print(cara)
    for slovo in TEXTS[2].split():
        vycistena_slova.append(slovo.strip(",.:;").lower())
    for slova in vycistena_slova:
        length = len(slova)
        if length in delka_slov:
            delka_slov[length] += 1
        else:
            delka_slov[length] = 1
    sorted_delka_slov = sorted(delka_slov.items(), key=lambda x: x[0])
    for length, count in sorted_delka_slov:
        if length < 10:
            print(f"{'  '}{length}|{'*' * count}{' ' * (18 - count)}|{count}")    
        else: 
            print(f"{' '}{length}|{'*' * count}{' ' * (18 - count)}|{count}")
else:
    print("wrong data, terminating the program..")
    quit()
