#AnyList 
class Pair:
   def __init__(self,first,rest):
      self.first = first
      self.rest = rest
   def __repr__(self):
      return "Pair({},{})".format(self.first, self.rest)
   def __eq__(self,other):
      return type(self) == type(other) and self.first == other.first and self.rest == other.rest

#empty_list None --> Pair
#creates an empty list
def empty_list():
   return None

#add Pair, int, any type --> Pair
#adds the value to the list at a specific index
def help_add(linked, index, value, count):
   if index == count:
      return Pair(value,linked)
   else:
      return Pair(linked.first, help_add(linked.rest, index, value, (count+1)))
def add(linked, index, value):
   return help_add(linked,index,value,0)


#length Pair --> int
#returns the length of a list
def length(numlist):
   if numlist == None:
      return 0
   count = 1
   if numlist.rest == None:
      return count
   else:
      count += length(numlist.rest)
   return count

#get Pair, int --> any type
#returns the value at a certain index
def get(linked, index):
   return help_get(linked, index, 0)
def help_get(linked, index, count):
   if index == count:
      return linked.first
   else:
      return help_get(linked.rest, index, (count+1))

#set Pair, int, any type --> Pair
#replaces the value at a given index with a given value
def help_set(linked, index, value, count):
   if index == count:
      return Pair(value,linked.rest)
   else:
      return Pair(linked.first, help_set(linked.rest, index, value, (count+1)))
def set(linked, index, value):
   return help_set(linked,index,value,0)

#remove Pair, int --> Pair
#removes the value at a given index
def help_remove(linked, index, count):
   if index == count:
      return linked.rest
   else:
      return Pair(linked.first, help_remove(linked.rest, index, (count+1)))
def remove(linked, index):
   return (get(linked, index), help_remove(linked,index,0))
