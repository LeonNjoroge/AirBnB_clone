#!/usr/bin/python3

"""this is the Unittest for BaseModel"""

import os
from models.review import Review
import time
from models import storage
import unittest
from datetime import datetime


class TestReview(unittest.TestCase):
    """this test BaseModel"""

    def test_init(self):
        """test blank basemodel init"""

        snap = datetime.now()
        review_a = Review()
        snap2 = datetime.now()

        self.assertIsInstance(review_a.id, str)
        self.assertTrue(len(review_a.id) > 0)
        self.assertTrue("Review." + review_a.id in storage.all().keys())

        self.assertIsInstance(review_a.created_at, datetime)
        self.assertLess(review_a.created_at, snap2)
        self.assertGreater(review_a.created_at, snap)

        self.assertIsInstance(review_a.updated_at, datetime)
        self.assertLess(review_a.updated_at, snap2)
        self.assertGreater(review_a.updated_at, snap)

        review_a.save()
        self.assertIsInstance(review_a.updated_at, datetime)
        self.assertGreater(review_a.updated_at, snap)
        self.assertGreater(review_a.updated_at, snap2)
        del review_a

    def test_init_dict(self):

        """test dict basemodel init"""
        dict_test = {
            "updated_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
            "id": "z3854b62-93fa-fbbe-27de-630706f8313c",
            "created_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
        }

        review_b = Review(**dict_test)

        self.assertIsInstance(review_b.id, str)
        self.assertTrue(len(review_b.id) > 0)
        self.assertTrue(review_b.id == dict_test["id"])

        self.assertIsInstance(review_b.created_at, datetime)
        self.assertTrue(
            review_b.created_at.isoformat("T") == dict_test["created_at"]
        )

        self.assertIsInstance(review_b.updated_at, datetime)
        self.assertTrue(
            review_b.updated_at.isoformat("T") == dict_test["updated_at"]
        )

        review_b.save()

        self.assertGreater(review_b.updated_at, review_b.created_at)

        del review_b

    def test_attribute(self):
        """another test"""
        review_c = Review()

        self.assertTrue(hasattr(review_c, "place_id"))
        self.assertTrue(hasattr(review_c, "user_id"))
        self.assertTrue(hasattr(review_c, "text"))

        self.assertIsInstance(review_c.place_id, str)
        self.assertIsInstance(review_c.user_id, str)
        self.assertIsInstance(review_c.text, str)
