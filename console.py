#!/usr/bin/python3
'''contains the entry point of the command interpreter'''

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''class definition'''
    prompt = "(hbnb) "
    classess = {'BaseModel': 'BaseModel'}

    def do_quit(self, line):
        '''quit to exit the interpreter'''
        return True

    def do_EOF(self, line):
        '''EOF to exit the interpreter'''
        return True

    def emptyline(self):
        '''do nothing'''
        pass

    def do_create(self, arguments):
        '''Creates a new instance'''
        if arguments:
            if arguments in self.classes:
                class_name = get_attr(sys.modules[__name__], arguments)
                instance = get_class()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
