class Trainer:
    bag = []
    pokemon = []
    name = ''
    
    def __init__(self,poke,name):
    	for p in poke:
    		self.pokemon.append(p)
    		self.name = name
    		#Hier Trank zu Bag hinzufügen
    
    def __str__(self):
        o = 0
        temp = ''
        for p in self.pokemon:
            o += 1
            temp += str(o) + '. ' + p['name'].title() + ' '
            print(temp)
        return temp

class Pokemon:
	name = ''
	attacken = []
	hp = 1
	level = 5
	moveset = []
	
	def __init__(self,poke):
		self.name = poke['name']
		self.moveset = poke['moves']
		self.level = poke['level']
		self.hp = poke['stats'][0]['base_stat']
		
poke = new Pokemon()