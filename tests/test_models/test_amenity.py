#!/usr/bin/python3
""" """
import unittest
import pep8
Amenity = amenity.Amenity
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os
from datetime import datetime
import inspect
import models
from models import amenity
from models.base_model import BaseModel
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestAmenityDocs(unittest.TestCase):
    '''
        Tests to check the documentation and style of Amenity class
    '''
    @classmethod
    def setUpClass(cls):
        '''
            Set up for the doc tests
        '''
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        '''
            Test that models/amenity.py conforms to PEP8.
        '''
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        '''
            Test that tests/test_models/test_amenity.py conforms to PEP8.
        '''
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        '''
            Test for the amenity.py module docstring
        '''
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        '''
            Test for the Amenity class docstring
        '''
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
