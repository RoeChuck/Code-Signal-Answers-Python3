# Check if all digits of the given integer are even.

# Example

# For n = 248622, the output should be
# solution(n) = true;
# For n = 642386, the output should be
# solution(n) = false.

def solution(n):
    return all([int(a) % 2 == 0 for a in str(n)])