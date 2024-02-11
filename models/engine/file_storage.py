#!/usr/bin/python3
"""the Storage File for the AirBnB Clone"""

import models
import json
from os.path import exists


class FileStorage:
    """the Class for the FileStorage"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """this returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """sets obj in __objects with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """this converts __objects to JSON file"""
        val = dict()

        for keys in self.__objects.keys():
            val[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, mode='w') as jsonfile:
            json.dump(val, jsonfile)

    def reload(self):
        """this converts the JSON file to __objects"""
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.amenity import Amenity
        from models.place import Place
        from models.base_model import BaseModel
        from models.user import User

        if exists(self.__file_path):
            with open(self.__file_path) as jsonfile:
                decereal = json.load(jsonfile)

            for keys in decereal.keys():
                if decereal[keys]['__class__'] == "BaseModel":
                    self.__objects[keys] = BaseModel(**decereal[keys])
                elif decereal[keys]['__class__'] == "Place":
                    self.__objects[keys] = Place(**decereal[keys])
                elif decereal[keys]['__class__'] == "Review":
                    self.__objects[keys] = Review(**decereal[keys])
                elif decereal[keys]['__class__'] == "User":
                    self.__objects[keys] = User(**decereal[keys])
                elif decereal[keys]['__class__'] == "Amenity":
                    self.__objects[keys] = Amenity(**decereal[keys])
                elif decereal[keys]['__class__'] == "State":
                    self.__objects[keys] = State(**decereal[keys])
                elif decereal[keys]['__class__'] == "City":
                    self.__objects[keys] = City(**decereal[keys])
