'''
8th January, 2017
Prompt: Given an array of integers, find whether it's possible to construct an
integer using all the digits of the numbers in the array such that it would be
divisible by n (where n is 1 <= n <= 9). If it's possible, return true, else
return false.
'''

from functools import reduce

'''
Function which generates all possible permutations of digits in a list,
in the most efficient way possible ( O(2^n) instead of O(n!) )

Input:
    digit_counter : int list (Counting the number of each digit to place)
    agg_string         : str (Aggregates of the permutation as it is generated)
Output:
    perm_list   : str list (a list of all string permutations of the digits)
'''
def genPermute(digit_counter, agg_string=""):
    # Given that we know that the digits are between 0 and 9 inclusive,
    # we can count the amount we're given of each digit, so we can generate
    # only unique permutations instead of factorial( len(digit_list) ) amount
    # of permutations

    # Base Case
    if sum(digit_counter) == 0:
        return [agg_string]

    # Recursive Case
    perm_list = []
    # For each possible digit 0 <= i <= 9
    for i in range(10):
        if digit_counter[i] > 0:
            # Copies counter, then adjusts it to 'use' one more of digit i
            curr_digit_counter = list(digit_counter) # deep copy
            curr_digit_counter[i] -= 1
            # Updates curr_string to end with digit i
            curr_string = agg_string + str(i)
            # Recursive Call
            perm_list += genPermute(curr_digit_counter, curr_string)

    return perm_list

'''
Function which brute forces whether or not a permutation of digits exists that
is divisible by a given divisor. A method of last resort.
Input:
    digit_list  : int list (The digits we're permuting in search of a solution)
    divisor     : int      (The divisor we're dividing permutations by)
Output:
    possible    : bool     (Whether or not a solution exists)
'''
def bruteForce(digit_list, divisor):
    # Counts the number of times each digit is seen in digit_list
    digit_counter = [0] * 10
    for digit in digit_list:
        digit_counter[digit] += 1

    # Generates all permutations of the digit_list using genPermute
    perm_list = genPermute(digit_counter)
    # Converts all entries in perm_list to int
    perm_list = [int(x) for x in perm_list]

    # Checks for a valid solution
    for perm_int in perm_list:
        if perm_int % divisor == 0:
            return True

    return False

'''
Input:
    n        : int (the number we're trying to divide the permutation of arr by)
    arr      : int array (the array from which we get the possible digits)
Output:
    possible : bool (whether it's possible to construct an n-divisible integer)
'''
def divisibleIntegers(n, arr):
    arr = map(lambda x : str(x), arr) # converts the int array to a string arr
    digit_string = reduce(lambda a,b: a + b, arr)
    digit_list   = [int(x) for x in digit_string]

    # Checks through all easy measures of determining divisibility
    if n == 1:
        return true # all numbers are divisible by 1

    if n == 2:
        for digit in digit_list:
            # If digit_list contains an even digit, we can construct an even num
            if digit % 2 == 0:
                return True
        return False

    if n == 3:
        # A number is divisible by 3 iff its digits add up to a multiple of 3
        return sum(digit_list) % 3 == 0

    if n == 4:
        # If we construct a num ending in 4 or 8, it is divisible by 4
        # If a num doesn't contain an even digit, it can't be divisible by 8
        seenEven = False
        for digit in digit_list:
            if digit == 8 or digit == 4:
                return True
            if digit % 2 == 0:
                seenEven = True

        if not seenEven:
            return False

    if n == 5:
        # A number is divisible by 5 iff it ends in 5 or 0
        for digit in digit_list:
            if digit % 5 == 0:
                return True
        return False

    if n == 6:
        # A num is divisible by 6 iff its digits add up to a multiple of 3,
        # and it is even
        if sum(digit_list) % 3 == 0:
            for digit in digit_list:
                if digit % 2 == 0:
                    return True
        return False

    if n == 7:
        # A num is definitely divisible by 7 if it ends in 7
        for digit in digit_list:
            if digit == 7:
                return True

    if n == 8:
        # If we construct a num ending in 8, it is divisible by 8
        # If a num doesn't contain an even digit, it can't be divisible by 8
        seenEven = False
        for digit in digit_list:
            if digit == 8:
                return True
            if digit % 2 == 0:
                seenEven = True

        if not seenEven:
            return False

    if n == 9:
        # A number is divisible by 9 iff its digits add up to a multiple of 9
        return sum(digit_list) % 9 == 0

    # Otherwise, we need to brute force the solution
    return bruteForce(digit_list, n)

assert (divisibleIntegers(2,[20,40,60]) == True)
assert (divisibleIntegers(3,[20,40,60]) == True)
assert (divisibleIntegers(7,[20,40,60]) == True)
