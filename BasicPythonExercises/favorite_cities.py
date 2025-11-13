class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmark = landmarks

bangued = City('Bangued', 'Philippines', 50000,['Casamata Hills', 'Apao Rolling Hills', 'Tineg Waterfalls'] )

print(vars(bangued))