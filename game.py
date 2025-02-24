import requests as req
import json
import pickle
import os
import klassen
from klassen import Trainer,Pokemon
 
base_url = 'https://pokeapi.co/api/v2/'

def check(p,g):
	if(p.hp <= 0):
		print('Du hast verloren')
		exit()
	elif(g.hp <= 0):
		print('Du hast gewonnen!')
		exit()

poke = Pokemon('pikachu',5)
poke1 = Pokemon('charmander',10)
poke2 = Pokemon(input('Waehle ein Pokemon-->'),5)
player = Trainer([poke2,poke,poke1],input('Wie lautet dein Name.-->'))
geg = Pokemon('pikachu',5)
print(poke.typ1.title())
print('Ein wildes ' + geg.name.title() + ' erscheint!')
while(True):
    aktpk = player.pokemon[0]
    print(f"{geg.hp} HP")
    print('Was wird ' + player.name + ' tun')
    print('1. Kampf 2.Pokemon 3.Beutel 4.Flucht')
    a = input()
    if(a == 'debug'):
        print(aktpk)
        print(aktpk.moveset)
    elif(a == '1'):
    	o = 0
    	wählbar = []
    	for move in aktpk.moveset:
    		if(o < 4):
    			wählbar.append(move)
    			o = o + 1
    			print(str(o) + '. ' + move['move']['name'])
    	ack = klassen.holmove(wählbar[i := int(input()) - 1]['move']['url'],wählbar[i]['move']['name'])
    	print(ack['name'])
    	try:
    		geg.hp -= ack['power']
    	except:
    		pass
    elif(a == '2'):
    	print(player)
    	a , b = 0 , int(input('Welches Pokemon?')) - 1
    	player.pokemon[a] , player.pokemon[b] = player.pokemon[b] , player.pokemon[a]
    elif(a == '3'):
    	print(player.bag)
    elif(a == '4'):
    	print('Du bist geflohen!')
    	exit()
    else:
    	print('Unbekannte Eingabe')
