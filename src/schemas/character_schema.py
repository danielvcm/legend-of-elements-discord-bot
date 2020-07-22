from . import stats_schema
from . import fortune_schema
from . import oaths_and_respects_schema
from . import animal_companion_schema
class CharacterSchema:
    def __init__(self,_id = None, userId = None, guildId = None, selected = True, playbookClass = None, name = None, chi = None, backstory = [],
        stats = None, fortune = None, oaths_and_respects = None, tags = None, moves = [], basic_moves_modifiers = [], look = [],
        chakras = [], gears = [], notes = [], other_moves = [], materials = [], animal_companions = [], finished = False, created_at = None,
        updated_at = None, deleted_at = None):
        self._id = _id
        self.userId = userId
        self.guildId = guildId
        self.selected = selected
        self.playbookClass = playbookClass
        self.name = name
        self.chi = chi
        self.backstory = backstory
        if stats != None:
            self.stats = stats
        else:
            self.stats = stats_schema.StatsSchema()
        if fortune != None:
            self.fortune = fortune
        else:
            self.fortune = fortune_schema.FortuneSchema()
        if oaths_and_respects != None:
            self.oaths_and_respects = oaths_and_respects
        else:
            self.oaths_and_respects = oaths_and_respects_schema.OathsAndRespectsSchema()
        self.tags = tags
        self.moves = moves
        self.basic_moves_modifiers = basic_moves_modifiers
        self.look = look
        self.chakras = chakras
        self.gears = gears
        self.notes = notes
        self.other_moves = other_moves
        self.materials = materials
        self.animal_companions = animal_companions
        self.finished = finished
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
    
    def to_dict(self):
        return{
            'userId': self.userId,
            'guildId': self.guildId,
            'selected': self.selected,
            'playbookClass': self.playbookClass,
            'name': self.name,
            'chi': self.chi,
            'backstory': self.backstory,
            'stats': self.stats.to_dict(),
            'fortune': self.fortune.to_dict(),
            'oaths_and_respects': self.oaths_and_respects.to_dict(),
            'tags': self.tags,
            'moves': self.moves,
            'basic_moves_modifiers': self.basic_moves_modifiers,
            'look': self.look,
            'chakras': self.chakras,
            'gears': self.gears,
            'notes': self.notes,
            'other_moves': self.other_moves,
            'materials': self.materials,
            'animal_companions': [item.to_dict() for item in self.animal_companions],
            'finished': self.finished,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'deleted_at': self.deleted_at
        }

def from_dict(character_dict):
    character = CharacterSchema()
    if '_id' in character_dict:
        character._id = character_dict['_id']
    if 'userId' in character_dict:
        character.userId = character_dict['userId']
    if 'guildId' in character_dict:
        character.guildId = character_dict['guildId']
    if 'selected' in character_dict:
        character.selected = character_dict['selected']
    if 'playbookClass' in character_dict:
        character.playbookClass = character_dict['playbookClass']
    if 'name' in character_dict:
        character.name = character_dict['name']
    if 'chi' in character_dict:
        character.chi = character_dict['chi']
    if 'backstory' in character_dict:
        character.backstory = character_dict['backstory']
    if 'stats' in character_dict:
        character.stats = stats_schema.from_dict(character_dict['stats'])
    if 'fortune' in character_dict:
        character.fortune = fortune_schema.from_dict(character_dict['fortune'])
    if 'oaths_and_respects' in character_dict:
        character.oaths_and_respects = character_dict['oaths_and_respects']
    if 'tags' in character_dict:
        character.tags = character_dict['tags']
    if 'moves' in character_dict:
        character.moves = character_dict['moves']
    if 'basic_moves_modifiers' in character_dict:
        character.basic_moves_modifiers = character_dict['basic_moves_modifiers']
    if 'look' in character_dict:
        character.look = character_dict['look']
    if 'chakras' in character_dict:
        character.chakras = character_dict['chakras']
    if 'gears' in character_dict:
        character.gears = character_dict['gears']
    if 'notes' in character_dict:
        character.notes = character_dict['notes']
    if 'other_moves' in character_dict:
        character.other_moves = character_dict['other_moves']
    if 'materials' in character_dict:
        character.materials = character_dict['materials']
    if 'animal_companions' in character_dict:
        character.animal_companions = [animal_companion_schema.from_dict(item) for item in character_dict['animal_companions']]
    if 'finished' in character_dict:
        character.finished = character_dict['finished']
    if 'created_at' in character_dict:
        character.created_at = character_dict['created_at']
    if 'updated_at' in character_dict:
        character.updated_at = character_dict['updated_at']
    if 'deleted_at' in character_dict:
        character.deleted_at = character_dict['deleted_at']
    return character