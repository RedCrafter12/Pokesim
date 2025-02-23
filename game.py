import requests as req
import json
 
base_url = 'https://pokeapi.co/api/v2/'

def holdirec(z):
	return json.loads(req.get(z).text)
 
def holsim(z):
    return json.loads(req.get(base_url + z).text)
 
poke = holsim('pokemon/pikachu')
print(poke['types'][0]['type']['name'].title())
NAME = input('Wie lautet dein Name.-->')
print('Ein wildes ' + poke['name'].title() + ' erscheint!')
while(1>0):
    print('Was wird ' + NAME + ' tun')
    print('1. Kampf 2.Pokemon 3.Beutel 4.Flucht')
    a = input()
    if(a == 'debug'):
        print(poke)
        print(poke['stats'])
        for i in poke:
        	print(i)
        print(poke['moves'])
    if(a == '1'):
    	o = 0
    	wählbar = []
    	for move in poke['moves']:
    		if(move['version_group_details'][0]['level_learned_at'] <= 20 & o < 4):
    			wählbar.append(move)
    			o = o + 1
    			print(str(o) + '. ' + move['move']['name'])
    	ack = holdirec(wählbar[int(input()) - 1]['move']['url'])
    	print(ack['name'])
