#!/usr/bin/python3
""" imourt module """

from models import BaseModel

class Review(BaseModel):

    def __init__(self, *args, **kwargs):

        review_attr = {"place_id": "", "user_id": "", "text": ""}
        [setattr(self, key, kwargs.pop(key, value)) for key, value in review_attr.items()]
        super().__init__(*args, **kwargs)
