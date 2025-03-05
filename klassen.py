import json
import pickle
import os
import requests as req
import formulas

base_url = 'https://pokeapi.co/api/v2/'

class Trainer:
     
    def __init__(self,poke,name):
    	self.pokemon = []
    	for p in poke:
    		self.pokemon.append(p)
    		self.name = name
    		#Hier Trank zu Bag hinzufügen
    
    
    def __str__(self):
        o = 0
        temp = ''
        for p in self.pokemon:
            o += 1
            temp += str(o) + '. ' + p.name.title() + ' '
            print(temp)
        return temp

class Typ:
	def __init__(self,typi):
		self.name = typi['name']
		self.effec = typi['damage_relations']

class Pokemon:
	hp = 1
	level = 5
	
	
	def __init__(self,nam,level):
		poke = holsim('pokemon/',nam)
		self.name = poke['name']
		self.moveset = poke['moves']
		self.level = level
		for stat in poke['stats']:
			if stat['stat']['name'] == 'hp':
				self.hp = formulas.hp_calc(stat['base_stat'],24 , 74 , 78)
		self.typ1 = Typ(holmove(poke['types'][0]['type']['url'],poke['types'][0]['type']['name']))
		try:
			self.typ2 = Typ(holmove(poke['types'][1]['type']['url'],poke['types'][1]['type']['name']))
		except:
			pass
		print(self.typ1.name)


def holmove(url,name):        #WIP
	if os.path.exists(name):
	    datei = open(name,'rb')
	    x = pickle.load(datei)
	    datei.close()
	    print('Supiii')
	else:
	    x = json.loads(req.get(url).text)
	    datei = open(x['name'],'ab')
	    pickle.dump(x,datei)
	    datei.close()
	return x

def holdirec(z):
	if os.path.exists(z.rsplit('/', 1)[1]):
	    datei = open(z.rsplit('/', 1)[1],'rb')
	    x = pickle.load(datei)
	    datei.close()
	    print('Supiii')
	else:
		x = json.loads(req.get(z).text)
		datei = open(x['name'],'ab')
		pickle.dump(x, datei)
		datei.close()
		print('Ohh')
	return x
 
def holsim(z,n):
    if os.path.exists(n):
    	datei = open(n,'rb')
    	x = pickle.load(datei)
    	datei.close()
    	print('Supiii')
    else:
    	x = json.loads(req.get(base_url + z + n).text)
    	datei = open(x['name'],'ab')
    	pickle.dump(x,datei)
    	datei.close()
    return x
