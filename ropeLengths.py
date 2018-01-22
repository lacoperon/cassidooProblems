'''
Let's say you have a bunch of rops of various lengths, and you want all of
them to be the same length. You have to find the shortest one, and cut all of
the ropes to be that length.
Input:
    ropeLengths : int array
Output:
    ropeCuts    : int array
'''
def ropeCutter(ropeLengths):
    return list(map(lambda x : x - min(ropeLengths), ropeLengths))

assert ropeCutter([1,2,3]) == [0,1,2]
assert ropeCutter([0,0,3]) == [0,0,3]
assert ropeCutter([]) == []
