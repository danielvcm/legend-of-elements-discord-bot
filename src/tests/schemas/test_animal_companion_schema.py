from ...schemas import animal_companion_schema

def test_empty_constructor():
    animal_test = animal_companion_schema.AnimalCompanionSchema()
    assert animal_test.name == None
    assert animal_test.species == None
    assert animal_test.animal == None
    assert animal_test.moves == []

def test_filled_constructor():
    animal_test = animal_companion_schema.AnimalCompanionSchema(name="Momo", species='Flying Lemour', animal=1, moves=['fly','get bugs'])
    assert animal_test.name == "Momo"
    assert animal_test.species == 'Flying Lemour'
    assert animal_test.animal == 1
    assert animal_test.moves == ['fly','get bugs']

def test_to_dict_with_empty_constructor():
    animal_test = animal_companion_schema.AnimalCompanionSchema()
    test_dict = animal_test.to_dict()
    assert test_dict['name'] == None
    assert test_dict['species'] == None
    assert test_dict['animal'] == None
    assert test_dict['moves'] == []

def test_to_dict_with_filled_constructor():
    animal_test = animal_companion_schema.AnimalCompanionSchema(name="Momo", species='Flying Lemour', animal=1, moves=['fly','get bugs'])
    test_dict = animal_test.to_dict()
    assert test_dict['name'] == "Momo"
    assert test_dict['species'] == 'Flying Lemour'
    assert test_dict['animal'] == 1
    assert test_dict['moves'] == ['fly','get bugs']

def test_from_dict_with_empty_dict():
    test_dict = {}
    animal_test = animal_companion_schema.from_dict(test_dict)
    assert animal_test.name == None
    assert animal_test.species == None
    assert animal_test.animal == None
    assert animal_test.moves == []

def test_from_dict_with_filled_dict():
    test_dict = {
        'name': "Momo",
        'species': 'Flying Lemour',
        'animal': 1,
        'moves': ['fly','get bugs']
    }
    animal_test = animal_companion_schema.from_dict(test_dict)
    assert animal_test.name == "Momo"
    assert animal_test.species == 'Flying Lemour'
    assert animal_test.animal == 1
    assert animal_test.moves == ['fly','get bugs']