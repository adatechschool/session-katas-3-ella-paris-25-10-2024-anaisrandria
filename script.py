# Importer le module json de la bibliothèque Python
import json

# Ouvrir le fichier .json grâce à la méthode .load()
with open("pokedex.json") as file:
    pokedex = json.load(file)

print(type(pokedex))
pokemons_data = pokedex["pokemon"]

# Création d'une classe Pokemon
class Pokemon(object):
    def __init__(self, id, name, type, weight):
        self.id = id
        self.name = name
        self.type = type
        self.weight = weight
    
    def getFeatures(self):
        print(f"🐣 Id : {self.id}")
        print(f"Nom : {self.name}")
        print(f"Type : {self.type}")
        print(f"Poids : {self.weight}\n")
        return (self.id, self.name, self.type, self.weight)

# Créer des objets dynamiques à partir du dictionnaire de Pokemon
all_pokemons = []
for data in pokemons_data:
    pokemon = Pokemon(data["id"], data["name"], data["type"], data["weight"])
    all_pokemons.append(pokemon)

for pokemon in all_pokemons:
    pokemon.getFeatures()    

# ---------- ETAPE 2 ----------#
# Combien y’a-t-il de Pokemon dans les données ?
print("Nombre de Pokemons :", len(pokemons_data))

#Quels sont ceux dont le poids est supérieur à 10 kg ?
def moreThan10():
    for i in range(len(pokemons_data)):
        weight_str = pokemons_data[i]["weight"]
        weight_split = weight_str.split(" ", 1)
        weight_nb = float(weight_split[0])
        if weight_nb >= 10:
            print(pokemons_data[i]["name"], "->", weight_str)
    return weight_str

moreThan10()

# Ecrire une fonction qui permet de les classer par ordre croissant de poids et afficher le résultat.
# def orderByWeight():
# weight = moreThan10
# def orderByWeight():




# Afficher les caractéristiques de chaque Pokemon OKKKK!!!
# all_pokemons = [Pokemon(pokemon["id"], pokemon["name"], pokemon["type"]) for pokemon in pokemons_data]

# for pokemon in all_pokemons:
#     print(f"🦄 Id: {pokemon.id}\n Name: {pokemon.name}\n Type: {pokemon.type}")
#     print()



