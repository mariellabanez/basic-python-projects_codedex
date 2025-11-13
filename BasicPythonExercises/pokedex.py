class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    
    def speak(self):
        pokemon_sound = print(self.name, "!", self.name, "!")
        return pokemon_sound
    
    def display_details(self):
        print("Entry Number: ", self.entry)
        print("Name: ", self.name)
        print("Type: ", self.types)
        print("Description: ", self.description)
        if self.is_caught == True:
            print(self.name, "has been caught!")
        else:
            print(self.name, "has not been caught")

pokemon = Pokemon(1, "Vulpix", "Fire", "a small, fox-like Pokémon with reddish-brown fur, six orange tails with curled tips, and a cream-colored underbelly.", True)

pokemon.display_details() #Display the attributes listed
pokemon.speak()

        