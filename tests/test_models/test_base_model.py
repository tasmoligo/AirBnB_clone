#!/usr/bin/python3
'''BaseModel unittest'''

import unittest
from models.base_model import BaseModel
import models
import os


class TestBaseModel(unittest.TestCase):
    '''Tests BaseModel class'''

    def test_docstring(self):
        '''
        tests if classes, modules, methods and functions
        have docstring
        '''
        msg = "Módulo does not have docstring"
        self.assertIsNotNone(models.base_model.__doc__, msg)
        msg = "Clase does not have docstring"
        self.assertIsNotNone(BaseModel.__doc__, msg)

    def test_executable_file(self):
        '''test if file has executable permission'''
        is_read_true = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_BaseModel(self):
        '''tests if an object is of type BaseModel'''
        my_object = BaseModel()
        self.assertIsInstance(my_object, BaseModel)

    def test_id(self):
        '''tests if id is unique'''
        my_objectId = BaseModel()
        my_objectId1 = BaseModel()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_str(self):
        '''checks if the output of str is in the specified format'''
        my_strobject = BaseModel()
        _dict = my_strobject.__dict__
        string1 = "[BaseModel] ({}) {}".format(my_strobject.id, _dict)
        string2 = str(my_strobject)
        self.assertEqual(string1, string2)

    def test_save(self):
        '''checks if date updates when save() executed'''
        my_objectupd = BaseModel()
        first_updated = my_objectupd.updated_at
        my_objectupd.save()
        second_updated = my_objectupd.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        '''
        checka if to_dict returns a dictionary and if adding a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.
        '''
        my_model = BaseModel()
        my_dict_model = my_model.to_dict()
        self.assertIsInstance(my_dict_model, dict)
        for key, value in my_dict_model.items():
            flag = 0
            if my_dict_model['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
