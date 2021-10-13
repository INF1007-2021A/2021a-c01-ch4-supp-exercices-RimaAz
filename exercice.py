#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):

	return len(string)%2 ==0



def get_num_char(string, char):
	compteur = 0
	for i in string:
		if i == char:
			compteur +=1
	return compteur


def get_first_part_of_name(name):
	first_name = name.split("-")[0]
	reponse = first_name[0].upper()+ first_name[1:].lower()
	return reponse


def get_random_sentence(animals, adjectives, fruits):
	choix_1=random.choice(animals)
	choix_2 = random.choice(adjectives)
	choix_3 = random.choice(fruits)
	return (f"Aujourd’hui, j’ai vu un {choix_1} s’emparer d’un panier {choix_2} plein de {choix_3}.")


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
