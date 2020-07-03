#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

lst = [2,2,0];
def count_evens(lst):
    l = [];
    for i in lst:
        if (i%2 == 0):
            l.append(i);
    abc = len(l);
    return abc


print(count_evens(lst))
