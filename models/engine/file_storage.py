#!/usr/bin/python3
"""Initializes the class for storage"""
import json
import os
import datetime


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Saves a new object in the storage."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            data = {k: v.to_dict()
                    if hasattr(v, 'to_dict') and
                    callable(getattr(v, 'to_dict'))
                    else str(v)
                    for k, v in FileStorage.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """Reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            FileStorage.__objects = obj_dict

    def classes(self):
        """Return valid class drctionary and their references"""
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel,
                   }
        return classes

    def attributes(self):
        """Return valid attribute classname type"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
        }
        return attributes
