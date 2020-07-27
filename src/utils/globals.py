import pytz
import os
class Globals:
    def __init__(self):
        self.timezone = pytz.timezone(os.getenv('TIMEZONE'))