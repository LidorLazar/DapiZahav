# Defined contact
import json


class Contact:
    name = ''
    cellular = ''

    def __init__(self, name='', cellular=''):
        self.name = name
        self.cellular = cellular

    def __str__(self):
        return json.dumps({'name': self.name, 'cellular': self.cellular})

