class StatsSchema:
    def __init__(self,natural=None,hot=None,solid=None,keen=None,fluid=None):
        self.natural = natural
        self.hot = hot
        self.solid = solid
        self.keen = keen
        self.fluid = fluid

    def from_dict(self, stats_dict):
        self.natural = None
        self.hot = None
        self.solid = None
        self.keen = None
        self.fluid = None

        if 'natural' in stats_dict:
            self.natural = stats_dict['natural']
        if 'hot' in stats_dict:
            self.hot = stats_dict['hot']
        if 'solid' in stats_dict:
            self.solid = stats_dict['solid']
        if 'keen' in stats_dict:
            self.keen = stats_dict['keen']
        if 'fluid' in stats_dict:
            self.fluid = stats_dict['fluid']
        return self

    def to_dict(self):
        return{
            "natural": self.natural,
            "hot": self.hot,
            "solid": self.solid,
            "keen": self.keen,
            "fluid": self.fluid
        }

def from_dict(stats_dict):
    stats_schema = StatsSchema()

    if 'natural' in stats_dict:
        stats_schema.natural = stats_dict['natural']
    if 'hot' in stats_dict:
        stats_schema.hot = stats_dict['hot']
    if 'solid' in stats_dict:
        stats_schema.solid = stats_dict['solid']
    if 'keen' in stats_dict:
        stats_schema.keen = stats_dict['keen']
    if 'fluid' in stats_dict:
        stats_schema.fluid = stats_dict['fluid']
    return stats_schema