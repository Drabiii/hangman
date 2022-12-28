import sys
import os

### Scripts: ###

### Globalna zmienna liczba życ ###
lzyc = 0


### Clear console ###
clear = lambda: os.system('cls')


### Wybór poziomu trudnosci ###
def poziom_trudnosci():
    global lzyc
    print()
    print("""Poziomy trudnosci:
    (1)-Łatwy: 5 żyć 
    (2)-Normalny: 3 życia
    (3)-Trudny: 1 życie
    """)
    print()
    diff = input("Wybierz poziom trudnosci:")
    while diff != str(1) and diff != str(2) and diff != str(3):
        diff = input("Wybierz poziom trudnosci:")
    else:
        if diff == str(1):
            lzyc = 5
            print()
            print("Wybrano poziom Łatwy!")
            print("Dostępna liczba żyć:", lzyc)
            print()
        elif diff == str(2):
            lzyc = 3
            print()
            print("Wybrano poziom Normalny!")
            print("Dostępna liczba żyć:", lzyc)
            print()
        elif diff == str(3):
            lzyc = 1
            print()
            print("Wybrano poziom Trudny!")
            print("Dostępna liczba żyć:", lzyc)
            print()
        else:
            print("Nie wybrałeś prawidłowego poziomu trundosci!")

    return poziom_trudnosci


### Numerowanie listy ###
def find_ind(word, litera):
    ind = []

    for index, letter_in_word in enumerate(word):
        if litera == letter_in_word:
            ind.append(index)

    return ind


### Aktualne informacje o grze ###
def stats():
    info_letters = ",".join(used_letters)
    print()
    print("".join(user_word))
    print("Pozostało prób:", lzyc)
    print(f"Użyte litery: [{info_letters}]")
    print()


### Basic Program and variable ###

poziom_trudnosci()

word = input("Wpisz słowo: ")
clear()
used_letters = []
user_word = []
print()
print("####   Wisielec   ####")
print()

### wstawianie "_" w liste user_word (szukane słowo) ###
for _ in word:
    user_word.append("_")

### Pętla Właściwa ###
while True:
    litera = str(input("Wprowadz litere: "))
    litera = litera[0]

    while litera in used_letters:
        print()
        print("Taka litera juz WYSTEPUJE!")
        litera = str(input("Wprowadz litere ponownie: "))
        litera = litera[0]
    else:
        used_letters.append(litera)

    found_ind = find_ind(word, litera)
    if len(found_ind) == 0:
        print()
        print(str.upper("nie ma takiej litery"))
        lzyc -= 1

        if lzyc <= 0:
            clear()
            print()
            print("Pozostała liczba żyć:", lzyc)
            print()
            print("Koniec gry :(")
            sys.exit(0)
    else:
        for index in found_ind:
            user_word[index] = litera

    if "".join(user_word) == word:
        clear()
        print()
        print("Wygrałeś!\n")
        print("Szukane słowo to:", word)
        print()
        sys.exit(0)

    stats()
