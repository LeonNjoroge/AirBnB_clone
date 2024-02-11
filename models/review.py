#!/usr/bin/python3
"""
the model Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    It has the
    Public class attributes:
    place_id: empty string
    user_id: empty string
    text: empty string
    """
    place_id = ""
    user_id = ""
    text = ""
