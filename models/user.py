#!/usr/bin/python3
""" user.py 
"""

from models import BaseModel

class User(BaseModel):
    """ Class user that inherit from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""