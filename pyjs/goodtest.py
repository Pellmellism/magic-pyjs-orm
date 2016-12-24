#import utils, shim
#import stdlib.utils as utils
#import stdlib.shim as shim
#import stdlib
#from stdlib import utils
#from stdlib import shim

#utils = stdlib.utils
#shim = stdlib.shim

import stdlib.utils
#  ##import stdlib.utils as utils


utils = stdlib.utils

def enum_liab_type(ltype):
   return utils.enum_helper(['a', 'b', 'c'], ltype)
   pass


class Column:
   def __init__(self, cType):
      self.cType = cType


class Dollar():
   val = Column('int')
   def __init__(self, val):
      self.val = val

   def format(self):
      return '$' + str(self.val)

class User():
   x = 5

   def __init__(self, first=None):
      self.first = first
      self.y = 35

   def get_sum(self):
      if self.first is None:
         return self.y
      else:
         return self.first + self.y

z = User()
print(z.get_sum())


print(User(10).get_sum())


enum_liab_type('b')

lst = [0, 1, 2, 3, 4]
string = "hello world"

print(lst[0:2])
print(string[3:5])

print(lst[3:])
print(lst[:2])

print(string[:-2])


