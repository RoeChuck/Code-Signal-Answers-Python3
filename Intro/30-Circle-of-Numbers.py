# Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

# Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

# Example

# For n = 10 and firstNumber = 2, the output should be
# solution(n, firstNumber) = 7.

# make list of range then
def mysolution(n, firstNumber):
    return list(range(n))[firstNumber-len(range(n))//2]

# Better mathmatical solution:
def notmysolution(n, firstNumber):
    return (firstNumber + n/2)%n

# Used the time module to check the time on both codes, they are the same