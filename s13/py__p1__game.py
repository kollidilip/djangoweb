###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# generate the three digit CODE
import random
digits = list(range(10))
random.shuffle(digits)
computercode = digits[:3]
print(computercode)

codebroke = False;
checklist = list();
# loop until the csode is broken ie codebroke is true
#while codebroke == False:
# user setion to input a code of his guessed
def inputprompt():
    userinput = input("Please enter your guess code : ")
    for inp in userinput:
        checklist.append(int(inp));
    return checklist
checklist = inputprompt()
while (codebroke != True):
    if (checklist == computercode):
        checklist = list();
        print("Perfect Guess!! You won")
        codebroke == True
        break;
    elif ((checklist[0] == computercode[0]) or (checklist[1] == computercode[1]) or (checklist[2] == computercode[2]) ):
        print("Match, please try for perfect match")
        checklist = list(); # nullify the previous input
        inputprompt()
    else:
        print("Nope")
        checklist = list(); # nullify the previous input
        inputprompt()
