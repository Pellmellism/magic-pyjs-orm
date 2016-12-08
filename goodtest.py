

class User():
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
