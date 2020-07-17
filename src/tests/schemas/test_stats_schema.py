from ...schemas import stats_schema

def test_empty_constructor():
    test_schema = stats_schema.StatsSchema()
    assert test_schema.natural == None
    assert test_schema.hot == None
    assert test_schema.solid == None
    assert test_schema.keen == None
    assert test_schema.fluid == None

def test_constructor_with_values():
    test_schema = stats_schema.StatsSchema(natural=1, hot=2,solid=1,keen=0,fluid=-1)
    assert test_schema.natural == 1
    assert test_schema.hot == 2
    assert test_schema.solid == 1
    assert test_schema.keen == 0
    assert test_schema.fluid == -1

def test_from_dict_with_empty_dict():
    test_dict = {}
    test_schema = stats_schema.from_dict(test_dict)
    assert test_schema.natural == None
    assert test_schema.hot == None
    assert test_schema.solid == None
    assert test_schema.keen == None
    assert test_schema.fluid == None

def test_from_dict_with_filled_dict():
    test_dict = {
        'natural':1,
        'hot': 2,
        'solid': 1,
        'keen':0,
        'fluid':-1
    }
    test_schema = stats_schema.from_dict(test_dict)
    assert test_schema.natural == 1
    assert test_schema.hot == 2
    assert test_schema.solid == 1
    assert test_schema.keen == 0
    assert test_schema.fluid == -1

def test_to_dict_with_empty_constructor():
    test_schema = stats_schema.StatsSchema()
    test_dict = test_schema.to_dict()
    assert test_dict['natural'] == None
    assert test_dict['hot'] == None
    assert test_dict['solid'] == None
    assert test_dict['keen'] == None
    assert test_dict['fluid'] == None

def test_to_dict_with_filled_constructor():
    test_schema = stats_schema.StatsSchema(natural=1, hot=2,solid=1,keen=0,fluid=-1)
    test_dict = test_schema.to_dict()
    assert test_dict['natural'] == 1
    assert test_dict['hot'] == 2
    assert test_dict['solid'] == 1
    assert test_dict['keen'] == 0
    assert test_dict['fluid'] == -1
