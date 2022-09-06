#!/usr/bin/python3

"""
    File storage.py file creation
"""
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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
            to_dict[key] = obj.to_dict()
            
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(to_dict, f, indent=4)

    def reload(self):
        ''' deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        '''

        try:
            with open(self.__file_path, 'r') as f_obj:
                data = json.load(f_obj)

            for obj_dict in data.values():
                key = f"{obj_dict['__class__']}.{obj_dict['id']}"
                FileStorage.__objects.\
                    setdefault(key, eval(obj_dict['__class__'])(**obj_dict))
                    
        except FileNotFoundError:
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
