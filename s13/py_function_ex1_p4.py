#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

str = "The"

def doubleChar(str):
  # CODE GOES HERE
  s = '';
  for i in str:
      s = s + 2*i;
  return s
print(doubleChar(str))
