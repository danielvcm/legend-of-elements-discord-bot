from ..schemas.character_schema import CharacterSchema
from ..schemas import character_schema
from ..databases.mongodb import MongoDB
from ..utils.globals import Globals
import datetime


class Character(CharacterSchema):
    def __init__(self,_id = None, user_id = None, guild_id = None, selected = True, playbook_class = None, name = None, chi = None, backstory = [],
        stats = None, fortune = None, oaths_and_respects = None, tags = None, moves = [], basic_moves_modifiers = [], look = [],
        chakras = [], gears = [], notes = [], other_moves = [], materials = [], animal_companions = [], finished = False, created_at = None,
        updated_at = None, deleted_at = None):
        super().__init__(_id, user_id, guild_id, selected, playbook_class, name, chi, backstory,
                    stats, fortune, oaths_and_respects, tags, moves, basic_moves_modifiers, look,
                    chakras, gears, notes, other_moves, materials, animal_companions, finished, created_at,
                    updated_at, deleted_at)
        db = MongoDB()
        db.connect()
        self.table = db.database.characters
     
    def insert(self):
        self.created_at = datetime.datetime.now(Globals().timezone)
        self.table.insert_one(self.to_dict())

    def update(self):
        self.updated_at = datetime.datetime.now(Globals().timezone)
        self.table.update_one({'_id':self._id},{'$set':self.to_dict()})
    
    def delete(self):
        self.deleted_at = datetime.datetime.now(Globals().timezone)
        self.table.update_one({'_id':self._id},{'$set':{'deleted_at':self.deleted_at}})
    
    def find_by_user_id_and_guild_id(self,user_id,guild_id):
        characters_mongo = self.table.find({'user_id':user_id,'guild_id':guild_id,'deleted_at': None})
        characters = []
        for character_mongo in characters_mongo:
            characters.append(from_dict(character_mongo))
        return characters
    
    def find_by_user_id(self,user_id):
        characters_mongo = self.table.find({'user_id':user_id,'deleted_at': None})
        characters = []
        for character_mongo in characters_mongo:
            characters.append(from_dict(character_mongo))
        return characters

    def find_by_guild_id(self,guild_id):
        characters_mongo = self.table.find({'guild_id':guild_id,'deleted_at': None})
        characters = []
        for character_mongo in characters_mongo:
            characters.append(from_dict(character_mongo))
        return characters

def from_character_schema(character_schema):
    return Character(_id = character_schema._id, user_id = character_schema.user_id, guild_id =character_schema.guild_id,
        selected = character_schema.selected, playbook_class = character_schema.playbook_class, name = character_schema.name,
        chi = character_schema.chi, backstory = character_schema.backstory, stats = character_schema.stats, fortune = character_schema.fortune,
        oaths_and_respects = character_schema.oaths_and_respects, tags = character_schema.tags, moves = character_schema.moves,
        basic_moves_modifiers = character_schema.basic_moves_modifiers, look = character_schema.look, chakras = character_schema.chakras,
        gears = character_schema.gears, notes = character_schema.notes, other_moves = character_schema.other_moves, materials = character_schema.materials,
        animal_companions = character_schema.animal_companions, finished = character_schema.finished, created_at = character_schema.created_at,
        updated_at = character_schema.updated_at, deleted_at = character_schema.deleted_at)

def from_dict(character_dict):
    schema = character_schema.from_dict(character_dict)
    return from_character_schema(schema)

