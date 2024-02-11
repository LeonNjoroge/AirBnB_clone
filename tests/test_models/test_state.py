#!/usr/bin/python3

"""this is a Unittest for BaseModel"""

import os
from models import storage
import time
from models.state import State
import unittest
from datetime import datetime


class TestState(unittest.TestCase):
    """test BaseModel"""

    def test_init(self):
        """test blank basemodel init"""
        snap = datetime.now()
        state_a = State()
        snap2 = datetime.now()

        self.assertIsInstance(state_a.id, str)
        self.assertTrue(len(state_a.id) > 0)
        self.assertTrue("State." + state_a.id in storage.all().keys())

        self.assertIsInstance(state_a.created_at, datetime)
        self.assertLess(state_a.created_at, snap2)
        self.assertGreater(state_a.created_at, snap)

        self.assertIsInstance(state_a.updated_at, datetime)
        self.assertLess(state_a.updated_at, snap2)
        self.assertGreater(state_a.updated_at, snap)

        state_a.save()
        self.assertIsInstance(state_a.updated_at, datetime)
        self.assertGreater(state_a.updated_at, snap)
        self.assertGreater(state_a.updated_at, snap2)

        del state_a

    def test_init_dict(self):

        """this test basemodel init"""

        dict_test = {
            "updated_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
            "id": "z3854b62-93fa-fbbe-27de-630706f8313c",
            "created_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
        }
        state_b = State(**dict_test)

        self.assertIsInstance(state_b.id, str)
        self.assertTrue(len(state_b.id) > 0)

        self.assertTrue(state_b.id == dict_test["id"])

        self.assertIsInstance(state_b.created_at, datetime)
        self.assertTrue(
            state_b.created_at.isoformat("T") == dict_test["created_at"]
        )

        self.assertIsInstance(state_b.updated_at, datetime)
        self.assertTrue(
            state_b.updated_at.isoformat("T") == dict_test["updated_at"]
        )

        state_b.save()
        self.assertGreater(state_b.updated_at, state_b.created_at)

        del state_b

    def test_attribute(self):
        """this is another test"""

        state_c = State()

        self.assertTrue(hasattr(state_c, "name"))
        self.assertIsInstance(state_c.name, str)
