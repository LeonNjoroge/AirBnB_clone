#!/usr/bin/python3
"""Unittest for BaseModel"""

import os
import time
from models.base_model import BaseModel
import unittest
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """this tests BaseModel"""

    def test_init(self):
        """this tests blank basemodel init"""
        snap = datetime.now()
        b_model_1 = BaseModel()
        snap2 = datetime.now()

        self.assertIsInstance(b_model_1.id, str)
        self.assertTrue(len(b_model_1.id) > 0)
        self.assertTrue("BaseModel." + b_model_1.id in storage.all().keys())

        self.assertIsInstance(b_model_1.created_at, datetime)
        self.assertLess(b_model_1.created_at, snap2)
        self.assertGreater(b_model_1.created_at, snap)

        self.assertIsInstance(b_model_1.updated_at, datetime)
        self.assertLess(b_model_1.updated_at, snap2)
        self.assertGreater(b_model_1.updated_at, snap)

        b_model_1.save()
        self.assertIsInstance(b_model_1.updated_at, datetime)
        self.assertGreater(b_model_1.updated_at, snap)
        self.assertGreater(b_model_1.updated_at, snap2)

        del b_model_1

    def test_init_dict(self):
        """this test dict basemodel init"""

        test_dict = {
            "updated_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
            "id": "z3854b62-93fa-fbbe-27de-630706f8313c",
            "created_at": datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat(
                "T"
            ),
        }
        b_model_2 = BaseModel(**test_dict)

        self.assertIsInstance(b_model_2.id, str)
        self.assertTrue(len(b_model_2.id) > 0)
        self.assertTrue(b_model_2.id == test_dict["id"])

        self.assertIsInstance(b_model_2.created_at, datetime)
        self.assertTrue(
            b_model_2.created_at.isoformat("T") == test_dict["created_at"]
        )
        self.assertIsInstance(b_model_2.updated_at, datetime)
        self.assertTrue(
            b_model_2.updated_at.isoformat("T") == test_dict["updated_at"]
        )
        b_model_2.save()
        self.assertGreater(b_model_2.updated_at, b_model_2.created_at)

        del b_model_2
