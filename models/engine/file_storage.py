#!/usr/bin/python3

"""
    File storage.py file creation
"""
from .base_model import BaseModel
import json
import models

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
         return FileStorage.__objects

    def new(self, obj):
         key = f"{obj.__class__.__name__}.{obj.id}"
         FileStorage.__objects[key] = obj

    def save(self):
        to_dict = {}
        for key, obj in FileStorage.__objects.items():
            key = f"{obj.__class__.__name__}.{obj.id}"
            to_save.setdefault(key, obj.to_dict())

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(to_dict, f, indent=4)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
               data = json.load(f)
        
            for obj_dict in data.values():
                key = f"{obj_dict['__class__']}.{obj_dict['id']}"

                FileStorage.__objects.\
                    setdefault(key, eval(obj_dict['__class__'])(**obj_dict))

        except FileNotFoundError as e:
            pass

    def delete(self, obj):
        class_name = obj.__class__.__name__
        id = obj.id
        key = f"{class_name}.{id}"

        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()
            return True

        return False
