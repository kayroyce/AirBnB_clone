#!/usr/nin/python3
""" class for state """

from models import BaseModel

class State(BaseModel):
    """ subClass of State """

    def __init__(self, *args, **kwargs):

        self.name = kwargs.pop("name", '')
        super().__init__(*args, **kwargs)
