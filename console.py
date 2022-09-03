#!/usr/bin/python3
"""Console.py"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Command Line Class
    """

    prompt = '(hbhb)'

    model_list = ["BaseModel"]

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Truel value will also exit the progrsm"""
        return True

    def do_emptyline(self):
        """ignore empty line"""
        return False

    def onecmd(self, args):
        if args == "quit":
            return self.do_quit(args)
        elif args == "EOF":
            return self.do_EOF(args)
        else:
            cmd.Cmd.onecmd(self, args)

    @classmethod
    def handle_errors(cls, args, **kwargs):
        if not args:
            print("** class name missing **")
            return True
        else:
            args = args.split(" ")

        n = len(args)
        if args[0] not in HBNBCommand.model_list:
            print("** class doesn't exist **")
            return True

        if 'command' not in kwargs:
            return False

        for arg in kwargs.values():
            if n < 2:
                print("** instance id missing **")
                return True
        return False

    def do_create(self, args):

        error = HBNBCommand.handle_errors(args)
        if error:
            return

        obj = eval(args)()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        error = HBNBCommand.handle_errors(args, command = "show")

        if error:
            return

        args = args.split(" ")

        objects = storage.all()
        key = ".".join(args)
        obj = objects.get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
