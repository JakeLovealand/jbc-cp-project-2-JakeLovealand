class List:
   def __init__(self, capacity = 100):
      self.value = [None]*capacity
      self.size = 0
      self.capacity = capacity
   def __repr__(self):
      return "List({},{},{})".format(self.value,self.size,self.capacity)
   def __eq__(self,other):
      return type(other) == List and self.value == other.value and self.size == other.size and self.capacity == other.capacity

#empty_list None --> List
#returns an empty_list
def empty_list():
   return List()

#add List, int, any type --> List
#adds a value at a specific index in a list
def add(lst,index,value):
   if index < 0 or index > length(lst):
      raise IndexError()
   temp1 = lst.value[index]
   temp2 = value
   for i in range(length(lst)+1-index):
      temp1 = lst.value[index+i]
      lst.value[index+i] = temp2
      temp2 = temp1
   lst.size += 1
   if lst.size == lst.capacity:
      lst = double_cap(lst)
   return lst

def double_cap(lst):
   l1 = List(lst.capacity*2)
   for i in range(length(lst)):
      add(l1,i,lst.value[i])
   return l1
#length List --> int
#returns length of list
def length(lst):
   return lst.size

#get List,int --> value
#returns the value at a given index
def get(lst,index):
   if index < 0 or index > length(lst) or length(lst) == 0:
      raise IndexError()
   return lst.value[index]

#set List,int,any type --> List
#sets a given index in a List to a given value
def set(lst,index,value):
   if index < 0 or index > length(lst) or length(lst) == 0:
      raise IndexError()
   lst.value[index] = value
   return lst

#remove List, int --> List
#removes the item at a given index
def remove(lst,index):
   if index < 0 or index > length(lst) or length(lst) == 0:
      raise IndexError()
   for i in range(length(lst)-index):
      lst.value[index+i] = lst.value[index+i+1]
   lst.size -= 1
   return lst
