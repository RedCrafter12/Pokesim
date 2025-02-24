import json
import pickle
import os

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
    

class Pokemon:
	hp = 1
	level = 5
	
	
	def __init__(self,nam,level):
		poke = holsim('pokemon/',nam)
		self.name = poke['name']
		self.moveset = poke['moves']
		self.level = level
		self.hp = poke['stats'][0]['base_stat']
		self.typ1 = poke['types'][0]['type']['name']
		try:
			self.typ2 = poke['types'][1]['type']['name']
		except:
			pass



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
	print(z.rsplit('/', 1)[-2])
	if os.path.exists(z.rsplit('/', 1)[-1]):
	    datei = open(z.rsplit('/', 1)[-1],'rb')
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
