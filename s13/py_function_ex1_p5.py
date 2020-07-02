#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3
a = 2;b= 1; c= 14;

def no_teen_sum(a,b,c):
  # CODE GOES HERE
  sum = 0;
  for i in [a,b,c]:
      z = fix_teen(i)
      sum = sum + fix_teen(i);
  return sum

def fix_teen(n):
  # CODE GOES HERE
  if ((13 <= n < 15) or (16 < n <= 19)):
      return 0;
  else:
      return n;



print(no_teen_sum(a,b,c))
