#!/bin/usr/python3

"""Creates a variable to initialize an instance of FileStorage"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()