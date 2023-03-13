#!/usr/bin/python3
'''user model'''
from models.base_model import BaseModel


class Useer(BaseModel):
    '''Inherits from BaseModel'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
