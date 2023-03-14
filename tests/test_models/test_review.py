#!/usr/bin/python3
'''Unittest for Review class'''
import unittest
import models
import os
from models.review import Review


class TestReview(unittest.TestCase):
    '''Tests class Review'''

    def test_docstring(self):
        '''
        test if funcions, methods, classes
        and modules have docstring
        '''
        msg = "Módulo does not has docstring"
        self.assertIsNotNone(models.review.__doc__, msg)
        msg = "Clase does not has docstring"
        self.assertIsNotNone(Review.__doc__, msg)

    def test_executable_file(self):
        '''tests if file has executable permission'''
        is_read_true = os.access('models/review.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/review.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/review.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_Review(self):
        '''tests if an object is of type Review'''
        my_object = Review()
        self.assertIsInstance(my_object, Review)

    def test_id(self):
        '''tests if id is unique'''
        my_object = Review()
        my_object_1 = Review()
        self.assertNotEqual(my_object.id, my_object_1.id)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        my_object = Review()
        _dict = my_object.__dict__
        string1 = "[Review] ({}) {}".format(my_object.id, _dict)
        string2 = str(my_object)
        self.assertEqual(string1, string2)

    def test_save(self):
        '''checks if date updates when saved'''
        my_object = Review()
        first_update = my_object.updated_at
        my_object.save()
        second_update = my_object.updated_at
        self.assertNotEqual(first_update, second_update)

    def test_to_dict(self):
        '''
        checksif to_dict returns a dictionary, if addingclass
        key with sclass name of the object and if updated_at and
        created_at are converted to string object in ISO format
        .'''
        my_model = Review()
        my_dict_model = my_model.to_dict()
        self.assertIsInstance(my_dict_model, dict)
        for key, value in my_dict_model.items():
            flag = 0
            if my_dict_model['__class__'] == 'Review':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
