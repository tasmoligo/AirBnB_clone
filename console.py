#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


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
        """Creates a new instance of the specified model class, saves it to a JSON file,
       and prints the assigned ID.
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
                print("** class name missing **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
               key = f"{args[0]}"
               if key not in storage.all():
                   print("** no instance found **") 
               else:
                   print(storage.all()[key])
                
        
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()