# Palindrome Rearranging

# Given a string, find out if its characters can be rearranged to form a palindrome.

# Example

# For inputString = "aabb", the output should be
# solution(inputString) = true.

# We can rearrange "aabb" to make "abba", which is a palindrome.

def solution(input_string):
    # to be a possible pallindrome: each letter must occur an even amount of times, (only one letter can have odd count)
    # since it can be in the middle of an odd-length letter and still make a pallindrome, if the rest of the letters are
    # even
    # so you make a list comprehension counting the count of letters % 2 which gives 0 if even 1 if odd
    # if sum of that list is more than 1, it means more than one of the letters has an odd count, so it can't be
    # rearranged to make a pallindrome
    return sum([input_string.count(a) % 2 for a in set(input_string)]) <= 1
