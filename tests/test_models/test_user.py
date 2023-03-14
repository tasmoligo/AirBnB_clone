#!/usr/bin/python3
'''Unittest for User class'''

import unittest
import models
import os
from models.user import User


class TestUser(unittest.TestCase):
    '''Tests for class User'''

    def test_docstring(self):
        '''test if funcions, methods, classes and modules have docstring'''
        msg = "Módulo does not has docstring"
        self.assertIsNotNone(models.user.__doc__, msg)
        msg = "Clase does not has docstring"
        self.assertIsNotNone(User.__doc__, msg)

    def test_executable_file(self):
        '''test if file has executable permission'''
        is_read_true = os.access('models/user.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/user.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/user.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_User(self):
        '''tests if an object is of type User'''
        my_object = User()
        self.assertIsInstance(my_object, User)

    def test_id(self):
        '''tests if id is unique'''
        my_object = User()
        my_object_1 = User()
        self.assertNotEqual(my_object.id, my_object_1.id)

    def test_str(self):
        '''checks if the output of str is in the specified format'''
        my_object = User()
        _dict = my_object.__dict__
        string_1 = "[User] ({}) {}".format(my_object.id, _dict)
        string_2 = str(my_object)
        self.assertEqual(string_1, string_2)

    def test_save(self):
        '''checks if date updates when saved'''
        my_object = User()
        first_update = my_object.updated_at
        my_object.save()
        second_update = my_object.updated_at
        self.assertNotEqual(first_update, second_update)

    def test_to_dict(self):
        '''
        checks if to_dict returns a dictionary, if adding a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.
        '''
        my_model = User()
        my_dict_model = my_model.to_dict()
        self.assertIsInstance(my_dict_model, dict)
        for key, value in my_dict_model.items():
            flag = 0
            if my_dict_model['__class__'] == 'User':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
