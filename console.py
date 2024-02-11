#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles End of file Charater"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty line that does nothing"""
        pass

    def do_create(self, line):
        """Creates a new instance of the specified model class
        saves it to a JSON file,and prints the assigned ID.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            class_obj = storage.classes()[line]
            obj = class_obj()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation
        of an instance based on the class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(args[0], instance_id)
                instances = storage.all()
                if key not in instances:
                    print("** no instance found **")
                else:
                    print(instances[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(args[0], instance_id)
                instances = storage.all()
                if key not in instances:
                    print("** no instance found **")
                else:
                    del instances[key]
                    storage.save()

    def do_all(self, line):
        """Prints the string representation of all instances."""
        if line != "":
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                instance = [str(obj) for key, obj in storage.all().items()
                            if type(obj).__name__ == args[0]]
                print(instance)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
