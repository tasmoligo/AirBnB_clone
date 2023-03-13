#!/usr/bin/python3
'''modules'''

from models.engine.file_storage import FileStorage

classes = {"BaseModel": "BaseModel", 'Amenity': 'Amenity', 'State': 'State',
           'Place': 'Place', 'Review': 'Review', 'User': 'User'}
storage = FileStorage()
storage.reload()
