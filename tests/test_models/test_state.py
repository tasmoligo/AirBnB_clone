#!/usr/bin/python3
'''Unittest for State class'''
import unittest
import models
import os
from models.state import State


class TestState(unittest.TestCase):
    '''Test for class State'''

    def test_docstring(self):
        '''
        test if funcions, methods, classes
        and modules have docstring
        '''
        msg = "Módulo does not has docstring"
        self.assertIsNotNone(models.state.__doc__, msg)
        msg = "Clase does not has docstring"
        self.assertIsNotNone(State.__doc__, msg)

    def test_executable_file(self):
        '''tests if file has executable permission'''
        is_read_true = os.access('models/state.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/state.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/state.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_State(self):
        '''test if an object is of type State'''
        my_object = State()
        self.assertIsInstance(my_object, State)

    def test_id(self):
        '''tests if id is unique'''
        my_object = State()
        my_object_1 = State()
        self.assertNotEqual(my_object.id, my_object_1.id)

    def test_str(self):
        '''checks if the output of str is in the specified format'''
        my_object = State()
        _dict = my_object.__dict__
        string_1 = "[State] ({}) {}".format(my_object.id, _dict)
        string_2 = str(my_object)
        self.assertEqual(string_1, string_2)

    def test_save(self):
        '''check if date update when save'''
        my_object = State()
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
        my_model = State()
        my_dict_model = my_model.to_dict()
        self.assertIsInstance(my_dict_model, dict)
        for key, value in my_dict_model.items():
            flag = 0
            if my_dict_model['__class__'] == 'State':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
