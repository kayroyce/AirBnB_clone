#!/usr/bin/python3

from .base_model import BaseModel
from .engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


storage = FileStorage()
storage.reload()
