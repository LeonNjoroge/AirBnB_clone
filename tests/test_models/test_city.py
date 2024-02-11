#!/usr/bin/python3
"""Unittest for BaseModel"""
import os
from models.city import City
import time
from models import storage
import unittest
from datetime import datetime


class TestCity(unittest.TestCase):
    """this test BaseModel"""

    def test_init(self):
        """test blank basemodel init"""
        snap = datetime.now()
        city_a = City()
        snap2 = datetime.now()

        self.assertIsInstance(city_a.id, str)
        self.assertTrue(len(city_a.id) > 0)
        self.assertTrue("City." + city_a.id in storage.all().keys())

        self.assertIsInstance(city_a.created_at, datetime)
        self.assertLess(city_a.created_at, snap2)
        self.assertGreater(city_a.created_at, snap)

        self.assertIsInstance(city_a.updated_at, datetime)
        self.assertLess(city_a.updated_at, snap2)
        self.assertGreater(city_a.updated_at, snap)

        city_a.save()

        self.assertIsInstance(city_a.updated_at, datetime)
        self.assertGreater(city_a.updated_at, snap)
        self.assertGreater(city_a.updated_at, snap2)

        del city_a

    def test_init_dict(self):
        """test dict basemodel init"""

        test_dict = {
            "updated_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
            "id": "z3854b62-93fa-fbbe-27de-630706f8313c",
            "created_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
        }

        city_b = City(**test_dict)

        self.assertIsInstance(city_b.id, str)
        self.assertTrue(len(city_b.id) > 0)
        self.assertTrue(city_b.id == test_dict["id"])

        self.assertIsInstance(city_b.created_at, datetime)
        self.assertTrue(
            city_b.created_at.isoformat("T") == test_dict["created_at"]
        )

        self.assertIsInstance(city_b.updated_at, datetime)
        self.assertTrue(
            city_b.updated_at.isoformat("T") == test_dict["updated_at"]
        )

        city_b.save()
        self.assertGreater(city_b.updated_at, city_b.created_at)
        del city_b

    def test_attribute(self):
        """another test"""
        city_c = City()

        self.assertTrue(hasattr(city_c, "state_id"))
        self.assertTrue(hasattr(city_c, "name"))

        self.assertIsInstance(city_c.state_id, str)
        self.assertIsInstance(city_c.name, str)
