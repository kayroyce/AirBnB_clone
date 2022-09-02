#!/usr/bin/python3
""" TestFileSturageDoc """

from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import pep8
import unittest
from datetime import datetime
import inspect

FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City, "Place": Place, "Review": Review, "State": State, "User": User}

class TestFileStorageDocs(unittest.TestCase):
    """ Checking the Documentation of file storage test """
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """ that models/engine/file_storage.py conforms to PEP8."""
         pep8s = pep8.StyleGuide(quiet=True)
         result = pep8s.check_files(['models/engine/file_storage.py'])
         self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """ tests/test_models/test_file_storage.py conforms to PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\test_file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """ file_storage.py module docstring test """
        self.assertIsNot(file_storage.__doc__, None, "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1, "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """ FileStorage class docstring test """
        self.assertIsNot(FileStorage.__doc__, None, "State class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1, "State class needs a docstring")

    def test_fs_func_docstrings(self):
        """ the presence of docstrings in FileStorage methods test """
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None, "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1, "{:s} method needs a docstring".format(func[0]))



class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        storage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        storage._FileStorage__objects = {}
