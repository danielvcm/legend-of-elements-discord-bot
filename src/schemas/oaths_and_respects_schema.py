class OathsAndRespectsSchema:
    def __init__(self,swear = [],respect = [], respected = []):
        self.swear = swear
        self.respect = respect
        self.respected = respected
    
    def to_dict(self):
        return{
            'swear': self.swear,
            'respect': self.respect,
            'respected': self.respected
        }

def from_dict(oaths_and_respects_dict):
    oaths_and_respects = OathsAndRespectsSchema()
    if 'swear' in oaths_and_respects_dict:
        oaths_and_respects.swear = oaths_and_respects_dict['swear']
    if 'respect' in oaths_and_respects_dict:
        oaths_and_respects.respect = oaths_and_respects_dict['respect']
    if 'respected' in oaths_and_respects_dict:
        oaths_and_respects.respected = oaths_and_respects_dict['respected']
    return oaths_and_respects