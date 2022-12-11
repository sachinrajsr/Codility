# correct solution
def solution(A, K):
    temp = [None]*len(A)

    for i in range(len(A)):
        temp[(i+K)%len(A)] = A[i]

    return temp


A, K = [1,2,3,4],2
print(solution(A, K))