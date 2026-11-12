import unittest
from pda_cfg.validators import *
class TestArithmetic(unittest.TestCase):
 def test_ok(self):
  for x in ['a','a+b','a*b','a+b*c','(a+b)*c']:self.assertTrue(validate_arithmetic(x))
 def test_bad(self):
  for x in ['a+','+a','a**b','(a+b','a+b)']:self.assertFalse(validate_arithmetic(x))
class TestParentheses(unittest.TestCase):
 def test_ok(self):
  for x in ['()','(())','()()','(()())','((()))']:self.assertTrue(validate_parentheses(x))
 def test_bad(self):
  for x in ['(',')','())(','(()','())']:self.assertFalse(validate_parentheses(x))
class TestPalindrome(unittest.TestCase):
 def test_ok(self):
  for x in ['a','b','aa','aba','abba','aabbaa']:self.assertTrue(validate_palindrome(x))
 def test_bad(self):
  for x in ['ab','aabb','abab','abb','aaba','abc']:self.assertFalse(validate_palindrome(x))
