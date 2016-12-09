#import utils, shim
import stdlib.utils
import stdlib.shim

utils = stdlib.utils
#shim = stdlib.shim

def enum_liab_type(ltype):
   return utils.enum_helper(['a', 'b', 'c'], ltype)

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

lst = [0, 1, 2, 3, 4]
string = "hello world"

print(lst[0:2])
print(string[3:5])

print(lst[3:])
print(lst[:2])

print(string[:-2])


