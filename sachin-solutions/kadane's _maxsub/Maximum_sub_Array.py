def solution(A):
    global_max = 0
    local_max = 0
    for i in range(1, len(A)):
        d = A[i] - A[i-1]
        local_max = max (d+local_max, d)
    
    global_max = max(local_max,global_max)

    return global_max
# only if there are negetive
    
