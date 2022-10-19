#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    return len(string) % 2 == 0



def remove_third_char(string: str) -> str:
    return string[0:2] + string[3:]

def replace_char(string: str, old_char: str, new_char: str) -> str:
    chaine = 'hello world!'
    ma_nouvelle_chaine = chaine.replace("w", "z")
    return ma_nouvelle_chaine


def get_number_of_char(string: str, char: str) -> int:
        compteur = 0
        for i in range (0,len(string)):
            if string[i] == char:
                compteur += 1
        return compteur



def get_number_of_words(sentence: str, word: str) -> int:
    words = sentence.split()
    number_of_word = 0
    for w in words:
        if w == word:
            number_of_word+= 1
    return number_of_word




def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(
        f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world est : {get_number_of_char(chaine, 'l')}")

    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()





