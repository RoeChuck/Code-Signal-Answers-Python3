# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

# Check if the given string is a correct variable name.

# Example

# For name = "var_1__Int", the output should be
# solution(name) = true;
# For name = "qq-q", the output should be
# solution(name) = false;
# For name = "2w2", the output should be
# solution(name) = false.

def solution(name):

    # list of char values that are acceptable (uppercase values ignored)
    charValues = [48,  49,  50,  51,  52,  53,  54,  55,  56,  57, 95, 97,  98,  99,  100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
  
    # make a list of all characters in variable name
    listName = [i for i in str(name)]

    #check if first character is a number, return False if it is
    if listName[0] in str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        return False
    
    #iterate through list of characters, check if char value is in charValues list, if not return False
    for i in range(len(listName)):
        if ord(listName[i].lower()) not in charValues:
            return False
    #return True if all values are in charValue list and variable name doesn't start with a number
    return True