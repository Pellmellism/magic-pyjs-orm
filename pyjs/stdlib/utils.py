


try:
   KK_IN_JS
except:
   KK_IN_JS = False


'''
if not KK_IN_JS:
   from . import shim
else:
   import shim
'''

if not KK_IN_JS:
   def __pragma__(a=None, b=None):
      pass
   __symbols__ = ['__py3.6__']

if KK_IN_JS:
   from org.transcrypt.stubs.browser import __pragma__

__pragma__('ifdef', '__py3.6__')
if '__py3.6__' in __symbols__:
   import sys, os
   #print(__file__)
   sys.path.append(os.path.dirname(os.path.realpath(__file__)))
__pragma__('endif')

   #sys.path.append('stdlib')

import shim

to_lower_case = shim.to_lower_case

#enum_arg = string in enum_list or int index in enum_list
def enum_helper(enum_list, enum_arg, to_index=None):
   options = [to_lower_case(x) for x in enum_list]

   if to_index is None:
      if enum_arg is None:
         return None
      elif type(enum_arg) is str:
         to_index = True
      elif type(enum_arg) is int:
         to_index = False
      else:
         raise "Bad type passed to stdlib.utils.enum_helper(%s)" % (str(enum_arg), )

   try:
      if to_index:
         return options.index(to_lower_case(enum_arg))
      else:
         return options[enum_arg]
   except Exception as e:
      pass
   return None


