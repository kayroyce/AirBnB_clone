#!/usr/bin/python3
""" Module with `user` class that inherates from BaseModel """

from models import BaseModel

class User(BaseModel):
    """ Class user that inherit from BaseModel """

    def ___init___(self, *args, **kwargs):
        """ init for User class """

        usr_attr = ["email", "password", "first_name", "last_name"]
        [setattr(self, key, kwargs.pop(key, "")) for key in usr_attr]

        super() .__init__(*args, **kwargs)

