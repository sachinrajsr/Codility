#fail O(n)
def solution(A, B, K):
    arr = list(range(A,B))
    count = 0
    for i in arr:
        if i%K == 0:
            count += 1
    return count


# O(1)

def solution(A, B, K):
    start = ceil(A/K)
    end = floor(B/K)
    return end-start+1