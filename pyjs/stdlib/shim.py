
try:
   KK_IN_JS
except:
   KK_IN_JS = False


def to_lower_case(string):
   if KK_IN_JS:
      return string.toLowerCase()
   else:
      return string.lower()

