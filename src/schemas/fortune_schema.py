class FortuneSchema:
    def __init__(self,max_fortune=None,current_fortune=None):
        self.max_fortune = max_fortune
        self.current_fortune = current_fortune

    def to_dict(self):
        return{
            'max_fortune': self.max_fortune,
            'current_fortune': self.current_fortune 
        }
    

def from_dict(fortune_dict):
    fortune_schema = FortuneSchema()
    if 'max_fortune' in fortune_dict:
        fortune_schema.max_fortune = fortune_dict['max_fortune']
    if 'current_fortune' in fortune_dict:
        fortune_schema.current_fortune = fortune_dict['current_fortune']
    return fortune_schema