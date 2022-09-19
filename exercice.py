#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Vérifier si le nombre de caractères d’une chaîne de caractères est pair
mon_nombre = int(input("Entrez un nombre: "))
if (mon_nombre % 2) == 0:
   print(str(mon_nombre) + " est Paire")
else:
   print(str(mon_nombre)  + " est impair")

#Supprimer le 3ème caractère d’une chaîne de caractères
chaine = input('entrez une chaine de charactere')
def remove_third_char(string: str) -> str:
    return string[:2] + string[3:]
print(chaine)





def is_even_len(string: str) -> bool:
    pass


def remove_third_char(string: str) -> str:
    pass


def replace_char(string: str, old_char: str, new_char: str) -> str:


    pass


def get_number_of_char(string: str, char: str) -> int:
    # Renvoyer le nombre d’occurrences d’un caractère dans une chaîne de caractères, sans utiliser de fonctions avancées
    compteur = 0
    for i in range (0, len(string)):
        if string[i] == char:
            compteur += 1
    return compteur
print(f"Le nb d'occurences de l dans hello est :{get_number_of_char(chaine, 'l')}")



def get_number_of_words(sentence: str, word: str) -> int:
    pass





