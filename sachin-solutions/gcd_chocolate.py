def hcf(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcf(b, a % b)
def solution(A,B):
    return A//hcf(A,B)