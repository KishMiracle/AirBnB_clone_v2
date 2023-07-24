#!/usr/bin/python3
<<<<<<< HEAD
""" """
from models.base_model import BaseModel, Base
from datetime import datetime
import unittest
from uuid import UUID
import json
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'basemodel test not supported')
class test_basemodel(unittest.TestCase):
    """ test class for base_model class"""

    def __init__(self, *args, **kwargs):
        """ init the test class of basemodel"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ the set up method of the test class"""
        pass

    def tearDown(self):
        """the teardown method of the ctest class"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_init(self):
        """Tests the initialization of the model class.
        """
        self.assertIsInstance(self.value(), BaseModel)
        if self.value is not BaseModel:
            self.assertIsInstance(self.value(), Base)
        else:
            self.assertNotIsInstance(self.value(), Base)

    def test_default(self):
        """ default testing of basemodel"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ testing basemodel with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ testing with kwargs again but with int kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save metthod"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ testing the str method of themodel"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ testing the to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)
        # Tests if it's a dictionary
        self.assertIsInstance(self.value().to_dict(), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', self.value().to_dict())
        self.assertIn('created_at', self.value().to_dict())
        self.assertIn('updated_at', self.value().to_dict())
        # Tests if to_dict contains added attributes
        mdl = self.value()
        mdl.firstname = 'Celestine'
        mdl.lastname = 'Akpanoko'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', self.value(firstname='Celestine').to_dict())
        self.assertIn('lastname', self.value(lastname='Akpanoko').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(self.value().to_dict()['created_at'], str)
        self.assertIsInstance(self.value().to_dict()['updated_at'], str)
        # Tests to_dict output
        datetime_now = datetime.today()
        mdl = self.value()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': mdl.__class__.__name__,
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertDictEqual(
                self.value(id='u-b34', age=13).to_dict(),
                {
                    '__class__': mdl.__class__.__name__,
                    'id': 'u-b34',
                    'age': 13
                }
            )
            self.assertDictEqual(
                self.value(id='u-b34', age=None).to_dict(),
                {
                    '__class__': mdl.__class__.__name__,
                    'id': 'u-b34',
                    'age': None
                }
            )
        # Tests to_dict output contradiction
        mdl_d = self.value()
        self.assertIn('__class__', self.value().to_dict())
        self.assertNotIn('__class__', self.value().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), mdl_d.__dict__)
        self.assertNotEqual(
            mdl_d.to_dict()['__class__'],
            mdl_d.__class__
        )
        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            self.value().to_dict(None)
        with self.assertRaises(TypeError):
            self.value().to_dict(self.value())
        with self.assertRaises(TypeError):
            self.value().to_dict(45)
        self.assertNotIn('_sa_instance_state', n)

    def test_kwargs_none(self):
        """ testing kwargs again with none"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ testing kwargs with one arg"""
        n = {'name': 'test'}
        new = self.value(**n)
        self.assertEqual(new.name, n['name'])

    def test_id(self):
        """ testing id attr of the model"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ testing created at attr"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """ testing updated at attr"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
=======
"""Defines unnittests for models/base_model.py."""
import os
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """BaseModel testing setup.

        Temporarily renames any existing file.json.
        Resets FileStorage objects dictionary.
        Creates a BaseModel instance for testing.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """BaseModel testing teardown.

        Restore original file.json.
        Delete the test BaseModel instance.
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

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/base_model.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.delete.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_attributes(self):
        """Check for attributes."""
        self.assertEqual(str, type(self.base.id))
        self.assertEqual(datetime, type(self.base.created_at))
        self.assertEqual(datetime, type(self.base.updated_at))

    def test_methods(self):
        """Check for methods."""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "delete"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_init(self):
        """Test initialization."""
        self.assertIsInstance(self.base, BaseModel)

    def test_two_models_are_unique(self):
        """Test that different BaseModel instances are unique."""
        bm = BaseModel()
        self.assertNotEqual(self.base.id, bm.id)
        self.assertLess(self.base.created_at, bm.created_at)
        self.assertLess(self.base.updated_at, bm.updated_at)

    def test_init_args_kwargs(self):
        """Test initialization with args and kwargs."""
        dt = datetime.utcnow()
        bm = BaseModel("1", id="5", created_at=dt.isoformat())
        self.assertEqual(bm.id, "5")
        self.assertEqual(bm.created_at, dt)

    def test_str(self):
        """Test __str__ representation."""
        s = self.base.__str__()
        self.assertIn("[BaseModel] ({})".format(self.base.id), s)
        self.assertIn("'id': '{}'".format(self.base.id), s)
        self.assertIn("'created_at': {}".format(repr(self.base.created_at)), s)
        self.assertIn("'updated_at': {}".format(repr(self.base.updated_at)), s)

    @unittest.skipIf(os.getenv("HBNB_ENV") is not None, "Testing DBStorage")
    def test_save(self):
        """Test save method."""
        old = self.base.updated_at
        self.base.save()
        self.assertLess(old, self.base.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("BaseModel.{}".format(self.base.id), f.read())

    def test_to_dict(self):
        """Test to_dict method."""
        base_dict = self.base.to_dict()
        self.assertEqual(dict, type(base_dict))
        self.assertEqual(self.base.id, base_dict["id"])
        self.assertEqual("BaseModel", base_dict["__class__"])
        self.assertEqual(self.base.created_at.isoformat(),
                         base_dict["created_at"])
        self.assertEqual(self.base.updated_at.isoformat(),
                         base_dict["updated_at"])
        self.assertEqual(base_dict.get("_sa_instance_state", None), None)

    @unittest.skipIf(os.getenv("HBNB_ENV") is not None, "Testing DBStorage")
    def test_delete(self):
        """Test delete method."""
        self.base.delete()
        self.assertNotIn(self.base, FileStorage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
>>>>>>> e6b3d3489ff16aa372d5bf7d1090bd04b06cf8bb
