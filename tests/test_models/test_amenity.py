#!/usr/bin/python3
"""The Unittest for Amenity model"""
import os
from datetime import datetime
from models import storage
from models.amenity import Amenity
import time
import unittest


class TestAmenity(unittest.TestCase):
    """test Amenity model"""
    def test_init(self):
        """test blank amenity init"""
        snap = datetime.now()
        amenity_a = Amenity()
        snap2 = datetime.now()

        self.assertIsInstance(amenity_a.id, str)
        self.assertTrue(len(amenity_a.id) > 0)
        self.assertTrue("Amenity." + amenity_a.id in storage.all().keys())

        self.assertIsInstance(amenity_a.created_at, datetime)
        self.assertLess(amenity_a.created_at, snap2)
        self.assertGreater(amenity_a.created_at, snap)

        self.assertIsInstance(amenity_a.updated_at, datetime)
        self.assertLess(amenity_a.updated_at, snap2)
        self.assertGreater(amenity_a.updated_at, snap)

        amenity_a.save()
        self.assertIsInstance(amenity_a.updated_at, datetime)
        self.assertGreater(amenity_a.updated_at, snap)
        self.assertGreater(amenity_a.updated_at, snap2)
        del amenity_a

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
        amenity_b = Amenity(**test_dict)

        self.assertIsInstance(amenity_b.id, str)
        self.assertTrue(len(amenity_b.id) > 0)
        self.assertTrue(amenity_b.id == test_dict["id"])

        self.assertIsInstance(amenity_b.created_at, datetime)
        self.assertTrue(
            amenity_b.created_at.isoformat("T") == test_dict["created_at"]
        )

        self.assertIsInstance(amenity_b.updated_at, datetime)
        self.assertTrue(
            amenity_b.updated_at.isoformat("T") == test_dict["updated_at"]
        )
        amenity_b.save()
        self.assertGreater(amenity_b.updated_at, amenity_b.created_at)

        del amenity_b

    def test_attribute(self):
        """another test"""
        amenity_c = Amenity()

        self.assertTrue(hasattr(amenity_c, "name"))
        self.assertIsInstance(amenity_c.name, str)
