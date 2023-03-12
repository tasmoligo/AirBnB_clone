#!/usr/bin/python3
'''Defining Base model'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''defining the base class'''
    def __init__(self, *args, **kwargs):
        '''The constructor'''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''Prints string representation of instances'''
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates the public instance attribute
        updated_at with the current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all
        keys/values of __dict__ of the instance'''
        dict_ = self.__dict__.copy()
        dict_['created_at'] = self.created_at.isoformat()
        dict_['updated_at'] = self.updated_at.isoformat()
        dict_['__class__'] = self.__class__.__name__
        return dict_
