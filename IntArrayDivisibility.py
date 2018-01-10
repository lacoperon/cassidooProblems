import math

'''
8th January, 2017
Prompt: Given an array of integers, find whether it's possible to construct an
integer using all the digits of the numbers in the array such that it would be
divisible by n (where n is 1 <= n <= 9). If it's possible, return true, else
return false.
'''

from functools import reduce
'''
Input:
    n : int (the number we're trying to divide the permutation of arr by),
    arr : int array (the array from which we get the possible digits)
Output:
    possible : bool (whether it's possible to construct an n-divisible integer)

TOFINISH: 4, 7, 8
'''
def divisibleIntegers(n, arr):
    arr = map(lambda x : str(x), arr) # converts the int array to a string arr
    digit_string = reduce(lambda a,b: a + b, arr)
    digit_list   = [int(x) for x in digit_string]
    print(digit_list)

    if n == 1:
        return true # all numbers are divisible by 1

    if n == 2:
        for digit in digit_list:
            if digit % 2 == 0: # any number ending in 0,2,4,6,8 is divisible by2
                return True
        return False

    if n == 3:
        return sum(digit_list) % 3 == 0

    if n == 4:
        divisibleByTwoAnywhere = False
        for digit in digit_list:
            if digit == 4:
                return True

        pass #TODO: finish this

    if n == 5:
        for digit in digit_list:
            if digit % 5 == 0:
                return True
        return False

    if n == 6:
        if sum(digit_list) % 3 == 0:
            for digit in digit_list:
                if digit % 2 == 0:
                    return True
        return False

    if n == 7:
        for digit in digit_list:
            if digit == 7:
                return True
        pass #TODO: finish this


    if n == 8:
        # Seeing if there's a good shortcut to determine divisibility by 8
        # (or an easy way to rule out divisibility)

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

        # Otherwise, we need to brute force a solution
        pass #TODO: implement this


    if n == 9:
        return sum(digit_list) % 9 == 0

def genPermute(digit_list, curr_string=""):
    if len(digit_list) == 0:
        return [curr_string]

    perm_list = []
    for index in range(len(digit_list)):
        l_digit_list = digit_list[0:index] # the left side of the digit list
        if index != len(digit_list):
            r_digit_list = digit_list[index+1:len(digit_list)]
        else:
            r_digit_list = []
        rem_digit_list = l_digit_list + r_digit_list # remaining unused digits
        curr_digit = str(digit_list[index])
        perm_list += genPermute(rem_digit_list, curr_string + curr_digit)
    return perm_list

assert len(genPermute([1,2,3,4,5,6,7,8,9,0], "")) == math.factorial(10)

# print(divisibleIntegers(4, [10,20,30]))
# print(divisibleIntegers(2, [1,2,3,4,5]))
