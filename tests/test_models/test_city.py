#!/usr/bin/python3
'''City unittest'''

import unittest
import models
import os
from models.city import City


class TestCity(unittest.TestCase):
    '''Tests for City class'''

    def test_docstring(self):
        '''test if funcions, methods, classes
        and modules have docstring'''
        msg = "Módulo does not has docstring"
        self.assertIsNotNone(models.city.__doc__, msg)
        msg = "Clase does not has docstring"
        self.assertIsNotNone(City.__doc__, msg)

    def test_executable_file(self):
        '''tests if file has executable permission'''
        is_read_true = os.access('models/city.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/city.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/city.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_city(self):
        '''tests if an object is of type city'''
        my_object = City()
        self.assertIsInstance(my_object, City)

    def test_id(self):
        '''tests if id is unique'''
        my_object_Id = City()
        my_object_IdA = City()
        self.assertNotEqual(my_object_Id.id, my_object_IdA.id)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        my_str_object = City()
        _dict = my_str_object.__dict__
        string_1 = "[City] ({}) {}".format(my_str_object.id, _dict)
        string_2 = str(my_str_object)
        self.assertEqual(string_1, string_2)

    def test_save(self):
        '''checks if date updates when saved'''
        my_object = City()
        first_update = my_object.updated_at
        my_object.save()
        second_update = my_object.updated_at
        self.assertNotEqual(first_update, second_update)

    def test_to_dict(self):
        '''
        checks if to_dict returns a dictionary, if adding a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format
        '''
        my_model = City()
        my_dict_model = my_model.to_dict()
        self.assertIsInstance(my_dict_model, dict)
        for key, value in my_dict_model.items():
            flag = 0
            if my_dict_model['__class__'] == 'City':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
