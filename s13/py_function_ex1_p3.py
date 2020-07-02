
#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True
a = "AbC"
b = "abXabcHiabc"

def end_other(a,b):
    z = min(len(a.lower()),len(b.lower()))
    if((a[-z:]).lower() == (b[-z:]).lower()):
        x = True;
    else:
        x = False;
    return x

print(end_other(a,b))
