#!/usr/bin/python3
<<<<<<< HEAD
"""This module instantiates an instance of the Storage will be used"""

from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
=======
"""Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
>>>>>>> e6b3d3489ff16aa372d5bf7d1090bd04b06cf8bb
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
<<<<<<< HEAD

=======
>>>>>>> e6b3d3489ff16aa372d5bf7d1090bd04b06cf8bb
storage.reload()
