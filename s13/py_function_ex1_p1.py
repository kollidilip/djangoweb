#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True
nums1 = [1, 1, 2, 3, 1]
nums2 = [1, 1, 2, 4, 1]
nums3 = [1, 1, 2, 1, 2, 3]

def arrayCheck(nums):
    x = set(nums)
    if(x == {1,2,3}):
        print("True")
    else:
        print("False")


arrayCheck(nums1)
arrayCheck(nums2)
arrayCheck(nums3)
