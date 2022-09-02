#!/usr/bin.python3
""" import modules """

from models import BaseModel

class Amenity(BaseModel):

    def __init__(self, *args, **kwargs):

        self.name = kwargs.pop("name", '')
        super().__init__(*args, **kwargs)
