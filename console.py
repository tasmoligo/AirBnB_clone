#!/usr/bin/python3
'''entry point of the command interpreter'''

import cmd
from models.base_model import BaseModel
from shlex import split
from models import storage
import sys
from user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''class definition'''
    prompt = "(hbnb) "
    classes = {'BaseModel': 'BaseModel'}

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
                class_name = getattr(sys.modules[__name__], arguments)
                instance = class_name()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arguments):
        '''Prints the string representation of an instance based on the class
        name and id'''
        arg = shlex.split(arguments)
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            store = models.storage.all()
            # Key has format <className>.id
            argus = arg[0] + '.' + str(arg[1])
            if argus in store:
                print(store[argus])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, arguments):
        ''' Deletes an instance based on the class name and id'''
        arg = shlex.split(arguments)
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            store = models.storage.all()
            # Key has format <className>.id
            join_arg = arg[0] + '.' + arg[1]
            if join_arg in store:
                del store[join_arg]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arguments):
        ''' Prints all string representation of all instances based or not on
        the class name'''
        arg = shlex.split(arguments)
        arg_list = []
        store = models.storage.all()
        if len(arg) == 0:
            for key in store:
                instances = str(dic[key])
                listI.append(instance)
            print(listI)
            return
        if arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            instance = ""
            for key in store:
                class_name = key.split('.')
                if class_name[0] == arg[0]:
                    instance = str(store[key])
                    arg_list.append(instance)
            print(arg_list)

    def do_update(self, arguments):
        ''' Updates an instance based on the class name and id by adding or
        updating attribute'''
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif len(arg) == 2:
            print("** attribute name missing **")
            return
        elif len(arg) == 3:
            print("** value missing **")
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        key = arg[0] + "." + arg[1]
        store = models.storage.all()
        try:
            store_key = store[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            key_type = type(getattr(store_key, arg[2]))
            arg[3] = key_type(arg[3])
        except AttributeError:
            pass
        setattr(store_key, arg[2], arg[3])
        models.storage.save()

    def do_count(self, aeguments):
        '''Retrieves the number of instances of a class'''
        arg = shlex.split(arguments)
        store = models.storage.all()
        num_of_instance = 0
        if arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in store:
                class_name = key.split('.')
                if class_name[0] == arg[0]:
                    num_of_instance += 1
            print(nu_of_instances)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
