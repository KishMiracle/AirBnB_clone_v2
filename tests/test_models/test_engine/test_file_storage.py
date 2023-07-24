#!/usr/bin/python3
<<<<<<< HEAD
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'fileStorage test not supported')
class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        new.save()
        storage.reload()
        loaded = None
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        new.save()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)
=======
"""Defines unnittests for models/engine/file_storage.py."""
import os
import json
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittests for testing the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """FileStorage testing setup.

        Temporarily renames any existing file.json.
        Resets FileStorage objects dictionary.
        Creates instances of all class types for testing.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()
        key = "{}.{}".format(type(cls.base).__name__, cls.base.id)
        FileStorage._FileStorage__objects[key] = cls.base
        cls.user = User()
        key = "{}.{}".format(type(cls.user).__name__, cls.user.id)
        FileStorage._FileStorage__objects[key] = cls.user
        cls.state = State()
        key = "{}.{}".format(type(cls.state).__name__, cls.state.id)
        FileStorage._FileStorage__objects[key] = cls.state
        cls.place = Place()
        key = "{}.{}".format(type(cls.place).__name__, cls.place.id)
        FileStorage._FileStorage__objects[key] = cls.place
        cls.city = City()
        key = "{}.{}".format(type(cls.city).__name__, cls.city.id)
        FileStorage._FileStorage__objects[key] = cls.city
        cls.amenity = Amenity()
        key = "{}.{}".format(type(cls.amenity).__name__, cls.amenity.id)
        FileStorage._FileStorage__objects[key] = cls.amenity
        cls.review = Review()
        key = "{}.{}".format(type(cls.review).__name__, cls.review.id)
        FileStorage._FileStorage__objects[key] = cls.review

    @classmethod
    def tearDownClass(cls):
        """FileStorage testing teardown.

        Restore original file.json.
        Delete all test class instances.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.storage
        del cls.base
        del cls.user
        del cls.state
        del cls.place
        del cls.city
        del cls.amenity
        del cls.review

    def test_pep8_FileStorage(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.delete.__doc__)

    def test_attributes(self):
        """Check for attributes."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_methods(self):
        """Check for methods."""
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "reload"))
        self.assertTrue(hasattr(FileStorage, "delete"))

    def test_init(self):
        """Test initialization."""
        self.assertTrue(isinstance(self.storage, FileStorage))

    def test_all(self):
        """Test default all method."""
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, FileStorage._FileStorage__objects)
        self.assertEqual(len(obj), 7)

    def test_all_cls(self):
        """Test all method with specified cls."""
        obj = self.storage.all(BaseModel)
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 1)
        self.assertEqual(self.base, list(obj.values())[0])

    def test_new(self):
        """Test new method."""
        bm = BaseModel()
        self.storage.new(bm)
        store = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, store.keys())
        self.assertIn(self.base, store.values())

    def test_save(self):
        """Test save method."""
        self.storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + self.base.id, save_text)
            self.assertIn("User." + self.user.id, save_text)
            self.assertIn("State." + self.state.id, save_text)
            self.assertIn("Place." + self.place.id, save_text)
            self.assertIn("City." + self.city.id, save_text)
            self.assertIn("Amenity." + self.amenity.id, save_text)
            self.assertIn("Review." + self.review.id, save_text)

    def test_reload(self):
        """Test reload method."""
        bm = BaseModel()
        with open("file.json", "w", encoding="utf-8") as f:
            key = "{}.{}".format(type(bm).__name__, bm.id)
            json.dump({key: bm.to_dict()}, f)
        self.storage.reload()
        store = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, store)

    def test_reload_no_file(self):
        """Test reload method with no existing file.json."""
        try:
            self.storage.reload()
        except Exception:
            self.fail

    def test_delete(self):
        """Test delete method."""
        bm = BaseModel()
        key = "{}.{}".format(type(bm).__name__, bm.id)
        FileStorage._FileStorage__objects[key] = bm
        self.storage.delete(bm)
        self.assertNotIn(bm, FileStorage._FileStorage__objects)

    def test_delete_nonexistant(self):
        """Test delete method with a nonexistent object."""
        try:
            self.storage.delete(BaseModel())
        except Exception:
            self.fail


if __name__ == "__main__":
    unittest.main()
>>>>>>> e6b3d3489ff16aa372d5bf7d1090bd04b06cf8bb
