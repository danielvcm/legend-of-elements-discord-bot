class AnimalCompanionSchema:
    def __init__(self, name = None, species = None, animal = None, moves = []):
        self.name = name
        self.species = species
        self.animal = animal
        self.moves = moves
    
    def to_dict(self):
        return{
            'name': self.name,
            'species': self.species,
            'animal': self.animal,
            'moves': self.moves
        }

def from_dict(animal_dict):
    animal_schema = AnimalCompanionSchema()
    if 'name' in animal_dict:
        animal_schema.name = animal_dict['name']
    if 'species' in animal_dict:
        animal_schema.species = animal_dict['species']
    if 'animal' in animal_dict:
        animal_schema.animal = animal_dict['animal']
    if 'moves' in animal_dict:
        animal_schema.moves = animal_dict['moves']
    return animal_schema
    
