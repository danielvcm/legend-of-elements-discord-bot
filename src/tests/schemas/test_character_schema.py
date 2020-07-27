from ...schemas import character_schema
from ...schemas import stats_schema
from ...schemas import fortune_schema
from ...schemas import oaths_and_respects_schema
from ...schemas import animal_companion_schema
from datetime import datetime

def test_empty_constructor():
    character_test = character_schema.CharacterSchema()
    assert character_test._id == None
    assert character_test.user_id == None
    assert character_test.guild_id == None
    assert character_test.selected == True
    assert character_test.playbook_class == None
    assert character_test.name == None
    assert character_test.chi == None
    assert character_test.backstory == []
    assert character_test.stats.natural == None
    assert character_test.stats.hot == None
    assert character_test.stats.solid == None
    assert character_test.stats.keen == None
    assert character_test.stats.fluid == None
    assert character_test.fortune.max_fortune == None
    assert character_test.fortune.current_fortune == None
    assert character_test.oaths_and_respects.swear == []
    assert character_test.oaths_and_respects.respect == []
    assert character_test.oaths_and_respects.respected == []
    assert character_test.tags == None
    assert character_test.moves == []
    assert character_test.basic_moves_modifiers == []
    assert character_test.look == []
    assert character_test.chakras == []
    assert character_test.gears == []
    assert character_test.notes == []
    assert character_test.other_moves == []
    assert character_test.materials == []
    assert character_test.animal_companions == []
    assert character_test.finished == False
    assert character_test.created_at == None
    assert character_test.updated_at == None
    assert character_test.deleted_at == None

def test_filled_constructor():
    stats_test = stats_schema.StatsSchema(natural=2,hot=1,solid=-1,keen=0,fluid=2)
    fortune_test = fortune_schema.FortuneSchema(max_fortune=2,current_fortune=1)
    oaths_test = oaths_and_respects_schema.OathsAndRespectsSchema(swear=['to love you'],respect=['my mom'], respected=['my dog'])
    animal_test = animal_companion_schema.AnimalCompanionSchema(name='Momo',species='Flying Lemour',animal=2,moves=['fly'])
    test_time = datetime.now()
    character_test = character_schema.CharacterSchema(_id='1ab2', user_id='2ba1', guild_id='2bc3', selected=False, playbook_class='Airshaper',
                    name='Aang', chi=5, backstory=['100 years frozen'], stats=stats_test, fortune=fortune_test, oaths_and_respects=oaths_test,
                    tags='mild',moves=['airshape'],basic_moves_modifiers=[{'attack':['+2','Nat']}],look=['bald','tatoos'],
                    chakras=['dont kill people'],gears=['staff'],notes=['avatar'],other_moves=['earthshaping'],materials=[2],
                    animal_companions=[animal_test],finished=True,created_at=test_time,updated_at=test_time,deleted_at=test_time)
    assert character_test._id == '1ab2'
    assert character_test.user_id == '2ba1'
    assert character_test.guild_id == '2bc3'
    assert character_test.selected == False
    assert character_test.playbook_class == 'Airshaper'
    assert character_test.name == 'Aang'
    assert character_test.chi == 5
    assert character_test.backstory == ['100 years frozen']
    assert character_test.stats == stats_test
    assert character_test.fortune == fortune_test
    assert character_test.oaths_and_respects == oaths_test
    assert character_test.tags == 'mild'
    assert character_test.moves == ['airshape']
    assert character_test.basic_moves_modifiers == [{'attack':['+2','Nat']}]
    assert character_test.look == ['bald','tatoos']
    assert character_test.chakras == ['dont kill people']
    assert character_test.gears == ['staff']
    assert character_test.notes == ['avatar']
    assert character_test.other_moves == ['earthshaping']
    assert character_test.materials == [2]
    assert character_test.animal_companions == [animal_test]
    assert character_test.finished == True
    assert character_test.created_at == test_time
    assert character_test.updated_at == test_time
    assert character_test.deleted_at == test_time

def test_to_dict_with_empty_constructor():
    character_test = character_schema.CharacterSchema()
    test_dict = character_test.to_dict()
    assert test_dict['user_id'] == None
    assert test_dict['guild_id'] == None
    assert test_dict['selected'] == True
    assert test_dict['playbook_class'] == None
    assert test_dict['name'] == None
    assert test_dict['chi'] == None
    assert test_dict['backstory'] == []
    assert test_dict['stats']['natural'] == None
    assert test_dict['stats']['hot'] == None
    assert test_dict['stats']['solid'] == None
    assert test_dict['stats']['keen'] == None
    assert test_dict['stats']['fluid'] == None
    assert test_dict['fortune']['max_fortune'] == None
    assert test_dict['fortune']['current_fortune'] == None
    assert test_dict['oaths_and_respects']['swear'] == []
    assert test_dict['oaths_and_respects']['respect'] == []
    assert test_dict['oaths_and_respects']['respected'] == []
    assert test_dict['tags'] == None
    assert test_dict['moves'] == []
    assert test_dict['basic_moves_modifiers'] == []
    assert test_dict['look'] == []
    assert test_dict['chakras'] == []
    assert test_dict['gears'] == []
    assert test_dict['notes'] == []
    assert test_dict['other_moves'] == []
    assert test_dict['materials'] == []
    assert test_dict['animal_companions'] == []
    assert test_dict['finished'] == False
    assert test_dict['created_at'] == None
    assert test_dict['updated_at'] == None
    assert test_dict['deleted_at'] == None


def test_to_dict_with_filled_dict():
    stats_test = stats_schema.StatsSchema(natural=2,hot=1,solid=-1,keen=0,fluid=2)
    fortune_test = fortune_schema.FortuneSchema(max_fortune=2,current_fortune=1)
    oaths_test = oaths_and_respects_schema.OathsAndRespectsSchema(swear=['to love you'],respect=['my mom'], respected=['my dog'])
    animal_test = animal_companion_schema.AnimalCompanionSchema(name='Momo',species='Flying Lemour',animal=2,moves=['fly'])
    test_time = datetime.now()
    character_test = character_schema.CharacterSchema(_id='1ab2', user_id='2ba1', guild_id='2bc3', selected=False, playbook_class='Airshaper',
                    name='Aang', chi=5, backstory=['100 years frozen'], stats=stats_test, fortune=fortune_test, oaths_and_respects=oaths_test,
                    tags='mild',moves=['airshape'],basic_moves_modifiers=[{'attack':['+2','Nat']}],look=['bald','tatoos'],
                    chakras=['dont kill people'],gears=['staff'],notes=['avatar'],other_moves=['earthshaping'],materials=[2],
                    animal_companions=[animal_test],finished=True,created_at=test_time,updated_at=test_time,deleted_at=test_time)
    test_dict = character_test.to_dict()
    assert test_dict['user_id'] == '2ba1'
    assert test_dict['guild_id'] == '2bc3'
    assert test_dict['selected'] == False
    assert test_dict['playbook_class'] == 'Airshaper'
    assert test_dict['name'] == 'Aang'
    assert test_dict['chi'] == 5
    assert test_dict['backstory'] == ['100 years frozen']
    assert test_dict['stats'] == stats_test.to_dict()
    assert test_dict['fortune'] == fortune_test.to_dict()
    assert test_dict['oaths_and_respects'] == oaths_test.to_dict()
    assert test_dict['tags'] == 'mild'
    assert test_dict['moves'] == ['airshape']
    assert test_dict['basic_moves_modifiers'] == [{'attack':['+2','Nat']}]
    assert test_dict['look'] == ['bald','tatoos']
    assert test_dict['chakras'] == ['dont kill people']
    assert test_dict['gears'] == ['staff']
    assert test_dict['notes'] == ['avatar']
    assert test_dict['other_moves'] == ['earthshaping']
    assert test_dict['materials'] == [2]
    assert test_dict['animal_companions'] == [animal_test.to_dict()]
    assert test_dict['finished'] == True
    assert test_dict['created_at'] == test_time
    assert test_dict['updated_at'] == test_time
    assert test_dict['deleted_at'] == test_time

def test_from_dict_with_empty_dict():
    test_dict = {}
    character_test = character_schema.from_dict(test_dict)
    assert character_test._id == None
    assert character_test.user_id == None
    assert character_test.guild_id == None
    assert character_test.selected == True
    assert character_test.playbook_class == None
    assert character_test.name == None
    assert character_test.chi == None
    assert character_test.backstory == []
    assert character_test.stats.natural == None
    assert character_test.stats.hot == None
    assert character_test.stats.solid == None
    assert character_test.stats.keen == None
    assert character_test.stats.fluid == None
    assert character_test.fortune.max_fortune == None
    assert character_test.fortune.current_fortune == None
    assert character_test.oaths_and_respects.swear == []
    assert character_test.oaths_and_respects.respect == []
    assert character_test.oaths_and_respects.respected == []
    assert character_test.tags == None
    assert character_test.moves == []
    assert character_test.basic_moves_modifiers == []
    assert character_test.look == []
    assert character_test.chakras == []
    assert character_test.gears == []
    assert character_test.notes == []
    assert character_test.other_moves == []
    assert character_test.materials == []
    assert character_test.animal_companions == []
    assert character_test.finished == False
    assert character_test.created_at == None
    assert character_test.updated_at == None
    assert character_test.deleted_at == None

def test_from_dict_with_filled_dict():
    stats_test = stats_schema.StatsSchema(natural=2,hot=1,solid=-1,keen=0,fluid=2)
    fortune_test = fortune_schema.FortuneSchema(max_fortune=2,current_fortune=1)
    oaths_test = oaths_and_respects_schema.OathsAndRespectsSchema(swear=['to love you'],respect=['my mom'], respected=['my dog'])
    animal_test = animal_companion_schema.AnimalCompanionSchema(name='Momo',species='Flying Lemour',animal=2,moves=['fly'])
    test_time = datetime.now()
    test_dict = {
        '_id': '1ab2',
        'user_id': '2ba1',
        'guild_id': '2bc3',
        'selected': False,
        'playbook_class': 'Airshaper',
        'name': 'Aang',
        'chi': 5,
        'backstory': ['100 years frozen'],
        'stats': stats_test.to_dict(),
        'fortune': fortune_test.to_dict(),
        'oaths_and_respects': oaths_test.to_dict(),
        'tags': 'mild',
        'moves': ['airshape'],
        'basic_moves_modifiers': [{'attack':['+2','Nat']}],
        'look': ['bald','tatoos'],
        'chakras': ['dont kill people'],
        'gears': ['staff'],
        'notes': ['avatar'],
        'other_moves': ['earthshaping'],
        'materials': [2],
        'animal_companions': [animal_test.to_dict()],
        'finished': True,
        'created_at': test_time,
        'updated_at': test_time,
        'deleted_at': test_time
        }
    character_test = character_schema.from_dict(test_dict)
    assert character_test._id == '1ab2'
    assert character_test.user_id == '2ba1'
    assert character_test.guild_id == '2bc3'
    assert character_test.selected == False
    assert character_test.playbook_class == 'Airshaper'
    assert character_test.name == 'Aang'
    assert character_test.chi == 5
    assert character_test.backstory == ['100 years frozen']
    assert character_test.stats.to_dict() == stats_test.to_dict()
    assert character_test.fortune.to_dict() == fortune_test.to_dict()
    assert character_test.oaths_and_respects.to_dict() == oaths_test.to_dict()
    assert character_test.tags == 'mild'
    assert character_test.moves == ['airshape']
    assert character_test.basic_moves_modifiers == [{'attack':['+2','Nat']}]
    assert character_test.look == ['bald','tatoos']
    assert character_test.chakras == ['dont kill people']
    assert character_test.gears == ['staff']
    assert character_test.notes == ['avatar']
    assert character_test.other_moves == ['earthshaping']
    assert character_test.materials == [2]
    assert character_test.animal_companions[0].to_dict() == animal_test.to_dict()
    assert character_test.finished == True
    assert character_test.created_at == test_time
    assert character_test.updated_at == test_time
    assert character_test.deleted_at == test_time
