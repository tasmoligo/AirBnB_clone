#!/usr/bin/python3
'''modules'''

from models.engine.file_storage import FileStorage

classes = {"BaseModel": "BaseModel"}
storage = FileStorage()
storage.reload()
