import unittest
from array_list import *

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
   
   def test_class(self):
      l1 = List(2)
      self.assertEqual(l1.capacity,2)
      self.assertEqual(l1.size,0)
      self.assertEqual(l1.value,[None]*2)
      self.assertEqual(repr(l1),"List([None, None],0,2)")
 
   def test_mt(self):
      self.assertEqual(empty_list(),List())

   def test_add(self):
      l1 = List(6)
      l2 = List(6)
      l2.size = 5
      l2.value = [1,2,3,4,5,None]
      for i in range(5):
         add(l1,i,i+1)
      self.assertEqual(l1,l2)
  
   def test_add_2(self):
      l1 = List(5)
      l2 = List(10)
      l2.size = 6
      l2.value = [1,2,3,4,5,6,None,None,None,None]
      for i in range(5):
         l1 = add(l1,i,i+1)
      l1 = add(l1,length(l1),6)
      self.assertEqual(l1,l2)

   def test_add_err(self):
      l1 = List(6)
      for i in range(5):
         add(l1,i,i+1)
      self.assertRaises(IndexError,add, l1,15,2)

   def test_get(self):
      l1 = List(6)
      l2 = List(6)
      l2.size = 5
      l2.value = [1,2,3,4,5,None]
      self.assertEqual(get(l2,2),3)

   def test_get_err(self):
      l1 = List(6)
      for i in range(5):
         add(l1,i,i+1)
      self.assertRaises(IndexError,get, l1,10)

   def test_set(self):
      l1 = List(6)
      l2 = List(6)
      l2.size = 5
      l2.value = [1,2,4,4,5,None]
      for i in range(5):
         add(l1,i,i+1)
      self.assertEqual(set(l1,2,4),l2)

   def test_set_err(self):
      l1 = List(6)
      for i in range(5):
         add(l1,i,i+1)
      self.assertRaises(IndexError,set,l1,10,2)

   def test_remove(self):
      l1 = List(5)
      l2 = List(10)
      l2.size = 4
      l2.value = [1,2,4,5,None,None,None,None,None,None]
      for i in range(5):
         l1 = add(l1,i,i+1)
      self.assertEqual(remove(l1,2),(3, l2))

   def test_remove_err(self):
      l1 = List(6)
      for i in range(5):
         add(l1,i,i+1)
      self.assertRaises(IndexError,remove, l1,15)

if __name__ == '__main__':
    unittest.main()
