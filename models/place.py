#!/usr/bin/python3
""" modele import """

from models import BaseModel

class Place(BaseModel):
    """ Sub class """

    def __init__(self, *args, **kwargs):
        """ Init method for `Place` class """
        place_attr = {"city_id": "", "user_id": "",
                      "name": "", "description": "",
                      "number_bathrooms": 0, "number_rooms": 0,
                      "max_guest": 0, "price_by_night": 0, "latitude": 0.0,
                      "longitude": 0.0, "amenity_ids": []}

        [setattr(self, key, kwargs.pop(key, default))
         for key, default in place_attr.items()]

        super().__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        """ Value validator then sets attr """

        place_attr = {"city_id": str, "user_id": str,
                      "name": str, "description": str,
                      "number_bathrooms": int, "number_rooms": int,
                      "max_guest": int, "price_by_night": int,
                      "latitude": float, "longitude": float,
                      "amenity_ids": list}

        # if passed wrong value then correct it
        if key in place_attr and type(value) != place_attr[key]:
                super().__setattr__(key, place_attr[key](value))
        else:  # for all other attr and right formated values
            super().__setattr__(key, value)