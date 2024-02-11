#!/usr/bin/python3

""" This is the Unittest for BaseModel"""

import os
from models import storage
from models.place import Place
import time
import unittest
from datetime import datetime


class TestPlace(unittest.TestCase):
    """this tests BaseModel"""

    def test_init(self):

        """this test blank basemodel init"""
        snap = datetime.now()
        place_a = Place()
        snap2 = datetime.now()

        self.assertIsInstance(place_a.id, str)
        self.assertTrue(len(place_a.id) > 0)
        self.assertTrue("Place." + place_a.id in storage.all().keys())

        self.assertIsInstance(place_a.created_at, datetime)
        self.assertLess(place_a.created_at, snap2)
        self.assertGreater(place_a.created_at, snap)

        self.assertIsInstance(place_a.updated_at, datetime)
        self.assertLess(place_a.updated_at, snap2)
        self.assertGreater(place_a.updated_at, snap)

        place_a.save()
        self.assertIsInstance(place_a.updated_at, datetime)
        self.assertGreater(place_a.updated_at, snap)
        self.assertGreater(place_a.updated_at, snap2)

        del place_a

    def test_init_dict(self):

        """this test dict basemodel init"""

        dict_test = {
            "updated_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
            "id": "z3854b62-93fa-fbbe-27de-630706f8313c",
            "created_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
        }
        place_b = Place(**dict_test)

        self.assertIsInstance(place_b.id, str)
        self.assertTrue(len(place_b.id) > 0)
        self.assertTrue(place_b.id == dict_test["id"])

        self.assertIsInstance(place_b.created_at, datetime)
        self.assertTrue(
            place_b.created_at.isoformat("T") == dict_test["created_at"]
        )

        self.assertIsInstance(place_b.updated_at, datetime)
        self.assertTrue(
            place_b.updated_at.isoformat("T") == dict_test["updated_at"]
        )

        place_b.save()
        self.assertGreater(place_b.updated_at, place_b.created_at)

        del place_b

    def test_attribute(self):
        """another test"""
        place_c = Place()

        self.assertTrue(hasattr(place_c, "city_id"))
        self.assertTrue(hasattr(place_c, "user_id"))
        self.assertTrue(hasattr(place_c, "longitude"))
        self.assertTrue(hasattr(place_c, "amenity_ids"))
        self.assertTrue(hasattr(place_c, "name"))
        self.assertTrue(hasattr(place_c, "description"))
        self.assertTrue(hasattr(place_c, "number_rooms"))
        self.assertTrue(hasattr(place_c, "number_bathrooms"))
        self.assertTrue(hasattr(place_c, "max_guest"))
        self.assertTrue(hasattr(place_c, "price_by_night"))
        self.assertTrue(hasattr(place_c, "latitude"))

        self.assertIsInstance(place_c.city_id, str)
        self.assertIsInstance(place_c.user_id, str)
        self.assertIsInstance(place_c.name, str)
        self.assertIsInstance(place_c.longitude, float)
        self.assertIsInstance(place_c.amenity_ids, list)
        self.assertIsInstance(place_c.description, str)
        self.assertIsInstance(place_c.number_rooms, int)
        self.assertIsInstance(place_c.number_bathrooms, int)
        self.assertIsInstance(place_c.max_guest, int)
        self.assertIsInstance(place_c.price_by_night, int)
        self.assertIsInstance(place_c.latitude, float)
