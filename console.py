#!/usr/bin/python3
'''console.py
'''

import cmd
import re
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User



def parse_line(line):
    '''parse_line function.

    Description: Gets a line and then parses it, then returns an array
    containing:
    The class name (string) (Always first element in array)
    The method name (string) (Always second element in array)
    The ID (string) (If available)
    The attribute name (string) (If available)
    The attribute value (string) (If available)
    '''
    result = []
    parameters = []
    args = line.split('.')
    if len(args) <= 1:
        return result
    else:
        class_name = args[0].strip()
        args = args[1].split('(')
        method_name = args[0].strip()
        args = args[1].split(',')
        result.extend([class_name, method_name])
        for i in range(len(args)):
            elem = args[i].strip(')')
            parameters.append(elem)
            for j in range(len(parameters)):
                elem = parameters[j]
                result.append((elem.strip()).strip('"'))
                return result


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    class_names = ["BaseModel", "User", "Place", "Review", "State", "Amenity", "City"]
    
    def emptyline(self):
        '''Is called when an empty line is passed to the console.
        '''
        pass

    def default(self, line):
        '''Defines the default behaviour of the program
        '''
        args = line.split()
        command = args[0].strip()
        line_str = ' '.join(args[1:])
        try:
            func = getattr(self, 'do_' + command)
        except AttributeError:
            print(f"*** Unknown syntax: {command}")
            return False
        response = func(line_str)
        if response is None:
            return False
        if response is True:
            return True


    def do_quit(self, line):
        '''
        This command quits the program
        '''
        return True

    def do_EOF(self, line):
        '''
        This command exits the program when CTRL+D is pressed
        '''
        return True


    def onecmd(self, line):
        '''Called when anything is passed in response to the prompt
        '''
        if line != '':
            line_args = parse_line(line)
            args_str = ' '
            if line_args != []:
                if len(line_args) ==3:
                    class_name, method, inst_id = line_args
                    args_str = ' '.join([class_name, inst_id])
                elif len(line_args) == 4:
                    class_name, method, inst_id, attr = line_args
                    args_str = ' '.join([class_name, inst_id, attr])
                elif len(line_args) ==5:
                    class_name, method, inst_id, attr, val = line_args
                    args_str = ' '.join([class_name, inst_id, attr, val])
                else:
                    return self.default(line)
                try:
                    func = getattr(self, 'do_' + method)
                except AttributeError:
                    print(f"Attribute Not Found: {'do_' + method}")
                return func(args_str)
            else:
                return self.emptyline()

    @classmethod
    def handle_errors(cls, args, **kwargs):
        if "all" in kwargs.values():
            if not args:
                return False

        if not args:
            print("** class name missing **")
            return True
        else:
            args = args.split(" ") # args becomes a list

        n = len(args)

        if args[0] not in HBNBCommand.model_list:
            print("** class doesn't exist **")
            return True


        if 'com' not in kwargs:
            return False
        
        for arg in kwargs.values():
            if arg in ["show", "destroy"]:
                if n < 2:
                    print("** instance id missing **")
                    return True

            if arg == "update":
                if n < 2:
                    print("** instance id missing **")
                    return True

                elif n < 3:
                    print("** attribute name missing **")
                    return True

                elif n < 4:
                    print("** value missing **")
                    return True
                


        return False

    def do_create(self, line):
        '''
        This command creates a new instance of a specified class.
        '''
        args = line.split()
        if len(args) != 1:
            print("** class name missing **")
        else:
            class_name = args[0].strip()
            if class_name in HBNBCommand.class_names:
                obj = eval(class-name)()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        '''Prints the string representation of an instance with the exact id
        '''
        args = line.split()
        if len(args) >= 1:
            class_name = args[0].strip()
            if class_name in HBNBCommand.class_names:
                if len(args) == 2:
                    search_id = args[1].strip()
                    search_key = "{}.{}".format(class_name, search_id)
                    storage.reload()
                    obj_dict = storage.all()
                    if search_key in obj_dict.keys():
                        obj = obj_dict[search_key]
                        print(obj)
                    else:
                        print("** no instance found **")
                    else:
                        print("** instance id missing **")
                    else:
                        print("** class doesn't exist **")
                    else:
                        print("** class name missing **")

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id
        '''
        args = line.split()
        if len(args) >= 1:
            class_name = args[0].strip()
            if class_name in HBNBCommand.class_names:
                if len(args) == 2:
                     search_id = args[1].strip()
                     search_key = "{}.{}".format(class_name, search_id)
                     storage.reload()
                     obj_dict = storage.all()
                     if search_key in obj_dict.keys():
                         storage.delete(search_key)
                     else:
                         print("** no instance found **")
                     else:
                         print("** instance id missing **")
                     else:
                         print("** class doesn't exist **")
                     else:
                         print("** class name missing **")

    def do_all(self, line):
        '''Prints the string form of all instances of the specified class name
        '''
        class_name = line.strip()
        if class_name in HBNBCommand.class_names or line == "":
            obj_dict = storage.all()
            if line:
                 obj_list = [str(item) for item in obj_dict.values()
                         if item.__class__.__name__ == class_name]
             else:
                 obj_list = [str(item) for item in obj_dict.values()]
                 print(obj_list)
             else:
                   print("** class doesn't exist **")

    def do_update(self, line):
        '''Updates an instance based on a class name and id.
        '''
        args = line.split()
        if len(args) >= 1:
            class_name = args[0]
            if class_name in HBNBCommand.class_names:
                if len(args) >= 2:
                     instance_id = args[1]
                     obj_dict = storage.all()
                     key = f"{class_name}.{instance_id}"
                     if key in obj_dict.keys():
                         obj = obj_dict[key]
                         if len(args) >= 3:
                             attribute_name = args[2]
                             if len(args) >= 4:
                                 value = args[3]
                                 setattr(obj, attribute_name, value)
                                 storage.new(obj)
                                 obj.save()
                             else:
                                 print("** value missing **")
                             else:
                                 print("** attribute name missing **")
                             else:
                                 print("** no instance found **")
                             else:
                                 print("** instance id missing **")
                             else:
                                 print("** class doesn't exist **")
                             else:
                                 print("** class name missing **")


if __name__ == "__main__":
     HBNBCommand().cmdloop()
