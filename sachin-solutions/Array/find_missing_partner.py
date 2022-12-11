# you can write to stdout for debugging purposes, e.g.
# "this is a debug message")


#Couldn't handle large numbers

def solution(A):
    result = 0
    Arr = array('i',A.sort())
    for i in set(A):
        if A.count(i) == 1:
            result = i
    return result


# Another Good
def solution(A):
    result = 0
    for i in A:
        result ^= A
    return result


# ANother good 
def solution(A):
    A.sort()
    A.append(-1)
    for i in range(0,len(A),2):
        if A[i] != A[i+1]:
            return A[i]