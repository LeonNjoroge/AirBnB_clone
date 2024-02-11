#!/usr/bin/python3
"""This Unittest for BaseModel"""
import os
from models import storage
import unittest
from datetime import datetime
from models.user import User
import time


class TestUser(unittest.TestCase):
    """this test BaseModel"""

    def test_ainit(self):

        """this test blank basemodel init"""
        snap = datetime.now()
        user_a = User()
        snap2 = datetime.now()

        self.assertIsInstance(user_a.id, str)
        self.assertTrue(len(user_a.id) > 0)
        self.assertTrue("User." + user_a.id in storage.all().keys())

        self.assertIsInstance(user_a.created_at, datetime)
        self.assertLess(user_a.created_at, snap2)
        self.assertGreater(user_a.created_at, snap)

        self.assertIsInstance(user_a.updated_at, datetime)
        self.assertLess(user_a.updated_at, snap2)
        self.assertGreater(user_a.updated_at, snap)

        user_a.save()
        self.assertIsInstance(user_a.updated_at, datetime)
        self.assertGreater(user_a.updated_at, snap)
        self.assertGreater(user_a.updated_at, snap2)
        del user_a

    def test_init_dict(self):

        """this tests dict basemodel init"""
        dict_test = {
            "updated_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
            "id": "z3854b62-93fa-fbbe-27de-630706f8313c",
            "created_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
        }
        user_b = User(**dict_test)

        self.assertIsInstance(user_b.id, str)
        self.assertTrue(len(user_b.id) > 0)

        self.assertTrue(user_b.id == dict_test["id"])

        self.assertIsInstance(user_b.created_at, datetime)
        self.assertTrue(
            user_b.created_at.isoformat("T") == dict_test["created_at"]
        )

        self.assertIsInstance(user_b.updated_at, datetime)
        self.assertTrue(
            user_b.updated_at.isoformat("T") == dict_test["updated_at"]
        )

        user_b.save()
        self.assertGreater(user_b.updated_at, user_b.created_at)
        del user_b

    def test_attribute(self):
        """this is another test"""
        user_c = User()

        self.assertTrue(hasattr(user_c, "email"))
        self.assertTrue(hasattr(user_c, "last_name"))
        self.assertTrue(hasattr(user_c, "password"))
        self.assertTrue(hasattr(user_c, "first_name"))

        self.assertIsInstance(user_c.email, str)
        self.assertIsInstance(user_c.last_name, str)
        self.assertIsInstance(user_c.password, str)
        self.assertIsInstance(user_c.first_name, str)
