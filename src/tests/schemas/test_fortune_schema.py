from ...schemas import fortune_schema

def test_empty_constructor():
    test_fortune = fortune_schema.FortuneSchema()
    assert test_fortune.max_fortune == None
    assert test_fortune.current_fortune == None

def test_filled_constructor():
    test_fortune = fortune_schema.FortuneSchema(max_fortune=2,current_fortune=1)
    assert test_fortune.max_fortune == 2
    assert test_fortune.current_fortune == 1

def test_to_dict_with_empty_constructor():
    test_fortune = fortune_schema.FortuneSchema()
    test_dict = test_fortune.to_dict()
    assert test_dict['max_fortune'] == None
    assert test_dict['current_fortune'] == None

def test_to_dict_with_filled_constructor():
    test_fortune = fortune_schema.FortuneSchema(max_fortune=2,current_fortune=1)
    test_dict = test_fortune.to_dict()
    assert test_dict['max_fortune'] == 2
    assert test_dict['current_fortune'] == 1

def test_from_dict_with_empty_dict():
    test_dict = {}
    test_fortune = fortune_schema.from_dict(test_dict)
    assert test_fortune.max_fortune == None
    assert test_fortune.current_fortune == None

def test_from_dict_with_filled_dict():
    test_dict = {
        'max_fortune': 2,
        'current_fortune': 1 
    }
    test_fortune = fortune_schema.from_dict(test_dict)
    assert test_fortune.max_fortune == 2
    assert test_fortune.current_fortune == 1