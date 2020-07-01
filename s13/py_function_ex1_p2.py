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
s2 = "Hi"
s3 = "Heeololeo"
def stringBits(str):
  # CODE GOES HERE
  s = '';
  for i in range(1,len(str)+1):
      if (i%2 != 0):
          s = s + str[i-1];
  return s

print(stringBits(s1))
print(stringBits(s2))
print(stringBits(s3))
