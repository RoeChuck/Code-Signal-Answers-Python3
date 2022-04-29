"""# almostIncreasingSequence # Given a sequence of integers as an array, determine whether it is possible to obtain
a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing
only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
solution(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
solution(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get
the strictly increasing sequence [1, 3]. """


# keep track of the running max (m) and previous max (pm) from sequence, and number of mistakes
# if mistakes > 1 during iteration, return False, exiting loop, saving time? See Big O notation for more information


def solution(sequence):
    cnt = 0
    # set to infinity to account for the sequence starting at a very negative value
    m = pm = float('-infinity')
    for e in sequence:
        if e > m:
            # first iteration should make pm = infinity (no change) and m = e
            pm, m = m, e
        # if the current iteration value is not greater than the running max,
        elif e > pm:  # check if current iteration value is greater than the previous max
            m = e  # sets new max to the running max
            cnt += 1  # increment mistakes counter
        else:
            cnt += 1
        # if at any point during iteration cnt is greater than 1, return false
        if cnt > 1:
            return False
    return True

# See alt solution branch for more a worse but working solution
