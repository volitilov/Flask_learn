import unittest
from app.models import User


class UserModelTestCash(unittest.TestCase):
  def test_password_setter(self):
    u = User(password='xxx')
    self.assertTrue(u.password_hash is not None)

  def test_no_password_getter(self):
    u = User(password='xxx')
    with self.assertRaises(AttributeError):
      u.password
  
  def test_password_verification(self):
    u = User(password='xxx')
    self.assertTrue(u.verify_password('xxx'))
    self.assertFalse(u.verify_password('iii'))

  def test_password_salts_are_random(self):
    u = User(password='xxx')
    u2 = User(password='xxx')
    self.assertTrue(u.password_hash != u2.password_hash)
