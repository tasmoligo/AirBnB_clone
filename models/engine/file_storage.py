#!/usr/bin/python3
'''Executes the class created'''
import json
from models.base_model import BaseModel


class FileStorage():
    '''serializes instances to a JSON file and
    deserializes JSON file to instances'''
    __file_path = "file.json"  # string - path to the JSON file (ex: file.json)
    __objects = []  # dictionary - store all objects by <class name>.id

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = obj.__class__.__name__ + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        json_object = {}
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(json_object, f)

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)'''

    try:
        with open(__file_path, "r", encoding="utf-8") as f:
            for key, value in json.load(f).items():
                _value = eval(value["__class__"])(**value)
                self.__objects[key] = _value
    except FileNotFoundError:
        pass
