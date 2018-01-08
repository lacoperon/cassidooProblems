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
        for digit in digit_list:
            if digit == 8:
                return True

        # TODO: Add rest of heuristic / brute force


    if n == 9:
        return sum(digit_list) % 9 == 0

# TODO: Fix this
def generatePermutation(digit_set, currentString=""):
    recursiveList = []
    for digit in digit_set:
        curr_digit_set = digit_set.copy()
        curr_digit_set.remove(digit)
        recursiveList.append([curr_digit_set, currentString+str(digit)])
    print recursiveList
    returnList = map(lambda (cset, cstring): generatePermutation(cset, cstring), recursiveList)
    print returnList
    returnList = reduce(lambda (l1,l2): l1 + l2, returnList)
    if len(digit_set) == 1:
        print returnList
        return returnList

generatePermutation(set([1,2,3]))





# def bruteForceDivisibility(digit_list, arr):
#     permutationList = []
#     for


print(divisibleIntegers(4, [10,20,30]))
print(divisibleIntegers(2, [1,2,3,4,5]))
