import unittest
from linked_list import *

class TestList(unittest.TestCase):
   # Note that this test doesn't assert anything! It just verifies your
   #  class and function definitions.

   def test_interface(self):
      temp_list = empty_list()
      temp_list = add(temp_list, 0, "Hello!")
      length(temp_list)
      get(temp_list, 0)
      temp_list = set(temp_list, 0, "Bye!")
      remove(temp_list, 0)

   def test_repr(self):
      l1 = Pair(1,None)
      self.assertEqual(repr(l1),"Pair(1,None)")
   def test_mt(self):
      l1 = empty_list()
      self.assertEqual(l1, None)
   
   def test_add(self):
      l1 = Pair(1,Pair(2,Pair(4,None)))
      self.assertEqual(add(l1,2,3),Pair(1,Pair(2,Pair(3,Pair(4,None)))))

   def test_add_err(self):
      l1 = Pair(1,Pair(2,None))
      self.assertRaises(IndexError,add,l1,10,2)

   def test_get(self):
      l1 = Pair(1,Pair(2,Pair(4,None)))
      self.assertEqual(get(l1,2),4)

   def test_get_err(self):
      l1 = Pair(1,Pair(2,None))
      self.assertRaises(IndexError,get,l1,10)

   def test_set(self):
      l1 = Pair(1,Pair(2,Pair(4,None)))
      self.assertEqual(set(l1,2,3),Pair(1,Pair(2,Pair(3,None))))

   def test_set_err(self):
      l1 = Pair(1,Pair(2,None))
      self.assertRaises(IndexError,set,l1,10,2)

   def test_remove(self):
      l1 = Pair(1,Pair(2,Pair(4,None)))
      self.assertEqual(remove(l1,2),(4, Pair(1,Pair(2,None))))

   def test_remove_err(self):
      l1 = Pair(1,Pair(2,None))
      self.assertRaises(IndexError,remove,l1,10)

   def test_length_mt(self):
      self.assertEqual(length(None),0)
   def test_length_1(self):
      l1 = Pair(1,Pair(2,Pair(-3,None)))
      self.assertEqual(length(l1),3)

if __name__ == '__main__':
    unittest.main()
