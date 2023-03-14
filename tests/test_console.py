#!/usr/bin/python3
'''tests the console'''

import sys
import models
from io import StringIO
from console import HBNBCommand
import unittest



class Test_HBNBConsole(unittest.TestCase):
    '''tests the console'''
    def setUp(self):
        '''setup for'''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        ''''''
        sys.stdout = self.backup

    def test_quit(self):
        ''' Tests quit'''
        instance = self.create()
        self.assertTrue(instance.onecmd("quit"))

    def create(self):
        ''' creates an instance'''
        return HBNBCommand()

    def test_EOF(self):
        ''' Tests EOF'''
        instance = self.create()
        self.assertTrue(instance.onecmd("EOF"))

    def test_all(self):
        ''' Test all'''
        instance = self.create()
        instance.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_show(self):
        '''Tests show'''
        instance = self.create()
        instance.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        instance.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

        def test_show_class_name(self):
            '''Tests the error messages for missing class name'''
            instance = self.create()
            instance.onecmd("create User")
            user_id = self.capt_out.getvalue()
            sys.stdout = self.backup
            self.capt_out.close()
            self.capt_out = StringIO()
            sys.stdout = self.capt_out
            instance.onecmd("show")
            x = (self.capt_out.getvalue())
            sys.stdout = self.backup
            self.assertEqual("** class name missing **\n", x)

        def test_show_class_id(self):
            '''test message error for missing id'''
            instance = self.create()
            instance.onecmd("create User")
            user_id = self.capt_out.getvalue()
            sys.stdout = self.backup
            self.capt_out.close()
            self.capt_out = StringIO()
            sys.stdout = self.capt_out
            console.onecmd("show User")
            x = (self.capt_out.getvalue())
            sys.stdout = self.backup
            self.assertEqual("** instance id missing **\n", x)

        def test_show_no_instance_found(self):
            '''Tests error message for missing id'''
            instance = self.create()
            instance.onecmd("create User")
            user_id = self.capt_out.getvalue()
            sys.stdout = self.backup
            self.capt_out.close()
            self.capt_out = StringIO()
            sys.stdout = self.capt_out
            instance.onecmd("show User " + "123456789")
            x = (self.capt_out.getvalue())
            sys.stdout = self.backup
            self.assertEqual("** no instance found **\n", x)

        def test_create(self):
            '''Tests that create works'''
            instance = self.create()
            instance.onecmd("create User")
            self.assertTrue(isinstance(self.capt_out.getvalue(), str))

        def test_class_name(self):
            '''
            Tests the error messages for missing class name'''
            instance = self.create()
            instance.onecmd("create")
            x = (self.capt_out.getvalue())
            self.assertEqual("** class name missing **\n", x)

        def test_class_name_doest_exist(self):
            '''Testing the error messages for class name missing'''
            instance = self.create()
            instance.onecmd("create Binita")
            x = (self.capt_out.getvalue())
            self.assertEqual("** class doesn't exist **\n", x)


            if __name__ == "__main__":
                unittest.main()
