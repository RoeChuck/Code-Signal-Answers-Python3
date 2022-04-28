# commonCharacterCount

"""
Given two strings, find the number of common characters between them.

Example:

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

# This one is a little different than the previous ones. Know the list.count() method


def solution(s1, s2):
    return sum([
        min(s1.count(a), 
            s2.count(a)) 
            for a in set(s1)
            ])

"""
LOGIC:
iterate through a set of any one of the strings and get count of each of the strings.
 
"""

# This one took me a while to figure out. I looked up the method for counting and during the process, ran
# into the solution online. I was writing similar code without the list comprehension. Not my code, but hey, 
# it's pretty.
# TODO: Update this with own code