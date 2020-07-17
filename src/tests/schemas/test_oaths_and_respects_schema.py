from ...schemas import oaths_and_respects_schema

def test_empty_constructor():
    oaths_test = oaths_and_respects_schema.OathsAndRespectsSchema()
    assert oaths_test.swear == []
    assert oaths_test.respect == []
    assert oaths_test.respected == []

def test_filled_constructor():
    oaths_test = oaths_and_respects_schema.OathsAndRespectsSchema(swear=['to tell the truth', 'to love you'],
                        respect=['my mom','my dad'], respected=['my kid', 'my dog'])
    assert oaths_test.swear == ['to tell the truth', 'to love you']
    assert oaths_test.respect == ['my mom','my dad']
    assert oaths_test.respected == ['my kid', 'my dog']

def test_to_dict_with_empty_constructor():
    oaths_test = oaths_and_respects_schema.OathsAndRespectsSchema()
    oaths_dict = oaths_test.to_dict()
    assert oaths_dict['swear'] == []
    assert oaths_dict['respect'] == []
    assert oaths_dict['respected'] == []

def test_to_dict_with_filled_constructor():
    oaths_test = oaths_and_respects_schema.OathsAndRespectsSchema(swear=['to tell the truth', 'to love you'],
                        respect=['my mom','my dad'], respected=['my kid', 'my dog'])
    oaths_dict = oaths_test.to_dict()
    assert oaths_dict['swear'] == ['to tell the truth', 'to love you']
    assert oaths_dict['respect'] == ['my mom','my dad']
    assert oaths_dict['respected'] == ['my kid', 'my dog']

def test_from_dict_with_empty_dict():
    oath_dict = {}
    oaths_test = oaths_and_respects_schema.from_dict(oath_dict)
    assert oaths_test.swear == []
    assert oaths_test.respect == []
    assert oaths_test.respected == []

def test_from_dict_with_filled_dict():
    oath_dict = {
        'swear': ['to tell the truth', 'to love you'],
        'respect': ['my mom','my dad'],
        'respected': ['my kid', 'my dog']
    }
    oaths_test = oaths_and_respects_schema.from_dict(oath_dict)
    assert oaths_test.swear == ['to tell the truth', 'to love you']
    assert oaths_test.respect == ['my mom','my dad']
    assert oaths_test.respected == ['my kid', 'my dog']