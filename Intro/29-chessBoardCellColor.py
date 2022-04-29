# Given two cells on the standard chess board, determine whether they have the same color or not.

# Example

# For cell1 = "A1" and cell2 = "C3", the output should be
# solution(cell1, cell2) = true.

# ord(a,c,e,h) is odd and ord(b,d,f) is even
# black = ord(aceh) + odd number or ord(bdf) + even number, both sum give even number bc odd + odd = even + even
# white is when this sum is odd
# given that, we can write a neat one line code:
def solution(cell1, cell2):
    return (ord(cell1[0]) + int(cell1[1])) % 2 == (ord(cell2[0]) + int(cell2[1])) % 2
