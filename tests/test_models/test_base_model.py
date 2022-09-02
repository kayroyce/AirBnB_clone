#!/usr/bin/python3
""" Expected Behavior and Documentations """

import models
import time
import inspect
from datetime import datetime
BaseModel + models.base_model.BaseModel
module_doc = models.base_model.__doc__

class TestBaseModelDocs(unittest.TestCase):
    """ Doccumentation stylke of BaseModel class """

    @classmethod
    def setUpClass(self):
        """ docstring setup """
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)
    
    def test_pep8_conformance(self):
        """ models/base_model.py conformint to PEP* """
        for path in ['models/base_model.py', 'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):

    def test_module_docstring(self):
        """ existence of module docstring """
        self.assertIsNot(module_doc, None, "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1, "base_model.py needs a docstring")

    def test_class_docstring(self):
        """ BaseModel class docstring """
        self.assertIsNot(BaseModel.__doc__, None, "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1, "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """ presence of docstrings in BaseModel methods """
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )



class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    @mock.patch('models.storage')
    def test_instantiation(self, mock_storage):
        """ if  object is correctly created """
        inst = BaseModel()
        self.assertIs(type(inst), BaseModel)

                        
