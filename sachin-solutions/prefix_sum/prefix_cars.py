# FAIL
def solution(A):
    array = []
    n = len(A)
    for i in range(n):
        array.append((A[i],A[n-i-1]))

    return -1 if len(array)>1000000000 else len(array)


#Car collision
def solution(A):
    possible_colision = 0
    count = 0

    for i in A:
        if i != 0:
            possible_colision += count
        else:
            count += 1

    return -1 if possible_colision>1000000000 else possible_colision
