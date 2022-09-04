#!/usr/bin/python3
""" TestConsoleDoc """

import console
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand

class TestConsoleDocs(unittest.TestCase):
    """ Class for console documentation testing """
    def test_pep8_conformance_console(self):
        """ To conform console to PEP8 """

        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """ Class for tests/test_console documentation testing """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for console.py module docstring"""
        self.assertIsNot(console.__doc__, None, "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1, "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """ the HBNBCommand class docstring testing """
        self.assertIsNot(HBNBCommand.__doc__, None, "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1, "HBNBCommand class needs a docstring")
