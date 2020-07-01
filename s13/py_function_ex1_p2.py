#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

s1 = "Hello"

def stringBits(str):
  # CODE GOES HERE
  s = '';
  for i in range(0,len(str)):
      if(i % 2 !=0 ):
          s = s + str[i];
          return s
bitstr = stringBits(s1)
print(bitstr)
