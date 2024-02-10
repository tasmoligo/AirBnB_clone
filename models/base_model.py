#!/usr/bin/python3
"""Define all common attribute/methods for other classes"""

import uuid
import datetime
from models import storage

class BaseModel:
    """Base Model"""

    def __init__(self, *args, **kwargs):
        
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
            

                
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)


    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts the object to a dictionary representation.

        Returns:
            A dictionary containing the object's attributes.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = data['created_at'].isoformat()
        data['updated_at'] = data['updated_at'].isoformat()

        return data
    
storage.reload()