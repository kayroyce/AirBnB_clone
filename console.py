import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command Line Class
    """

    prompt ='(hbhb)'

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Truel value will also exit the progrsm"""
        return True

    def do_emptyline(self):
        """ignore empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
