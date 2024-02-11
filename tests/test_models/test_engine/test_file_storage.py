#!/usr/bin/python3
"""uthis is unittest for filestorage"""

import json
import unittest
import os
from models.engine.file_storage import FileStorage
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """the class to test FileSTorage"""

    def test_class_variables(self):
        """ the var test"""
        file_store1 = FileStorage()
        list_ap = []


        if os.path.exists("file.json"):
            os.remove("file.json")

        for exists in file_store1.all().keys():
            list_ap.append(file_store1.all()[exists])

        for exists in list_ap:
            del file_store1.all()[exists.__class__.__name__ + "." + exists.id]

        self.assertFalse(hasattr(FileStorage, "__file_path"))
        self.assertFalse(hasattr(FileStorage, "__objects"))

        self.assertFalse(hasattr(file_store1, "__file_path"))
        self.assertFalse(hasattr(file_store1, "__objects"))

        del file_store1

        if os.path.exists("file.json"):
            print("file still exists")
            os.remove("file.json")

    def test_all(self):

        """this tests all"""
        file_store2 = FileStorage()
        list_ap = []

        if os.path.exists("file.json"):
            os.remove("file.json")

        for exists in file_store2.all().keys():
            list_ap.append(file_store2.all()[exists])

        for exists in list_ap:
            del file_store2.all()[exists.__class__.__name__ + "." + exists.id]

        self.assertIsInstance(file_store2.all(), dict)
        self.assertEqual(file_store2.all(), {})
        base_model1, base_model2 = BaseModel(), BaseModel()

        file_store2.new(base_model1)
        file_store2.new(base_model2)

        self.assertEqual(
            file_store2.all(), {"BaseModel." + base_model1.id: base_model1, "BaseModel." + base_model2.id: base_model2}
        )

        del base_model1, base_model2, file_store2

    def test_new(self):
        """test new"""
        diction = {
            "id": "8d8b4200-z106-469d-aec9-70zae1224150",
            "__class__": "BaseModel",
            "updated_at": "2020-07-01T16:47:21.260793",
            "created_at": "2020-07-01T16:47:21.260752",
        }
        file_store3 = FileStorage()
        list_ap = []
        if os.path.exists("file.json"):
            os.remove("file.json")

        for exists in file_store3.all().keys():
            list_ap.append(file_store3.all()[exists])

        for exists in list_ap:
            del file_store3.all()[exists.__class__.__name__ + "." + exists.id]
        classes = [
            Amenity(**diction),
            BaseModel(**diction),
            City(**diction),
            Place(**diction),
            Review(**diction),
            State(**diction),
            User(**diction),
        ]

        for clss in classes:
            file_store3.new(clss)
            self.assertIn(clss.__class__.__name__ + "." + clss.id, file_store3.all())

        for clss in classes:
            name = clss.__class__.__name__
            self.assertTrue(name + "." + clss.id in file_store3.all().keys())

        for m in range(len(file_store3.all().keys())):
            self.assertIn(file_store3.all()[list(file_store3.all().keys())[m]], classes)
        for exists in classes:
            del exists

        del file_store3
