# Importer le module json de la bibliothèque Python
import json

# Ouvrir le fichier .json grâce à la méthode .load()
with open("pokedex.json") as file:
    pokedex = json.load(file)

print(type(pokedex))
pokemons = pokedex["pokemon"]

class Pokemon(object):
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
    
    def getFeatures(self):
        print(f"Je m'appelle {self.name}, je suis de type {self.type}")


for i in range(len(pokemons)):
    print("\n🐣", pokemons[i])
    print(pokemons["name"])
    


pikachu = Pokemon(1, "Pikachu", "Feu")
pikachu.getFeatures()


