#!/usr/bin/python3
"""import from model """

from models import BaseModel

class City(BaseModel):
    """ Sub class """

    def __init__(self, *args, **kwargs):
        """ init method for lass of City """

        sef.state_id = kwargs.pop("name", '')
        super().__init__(*args, **kwargs)


