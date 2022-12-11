def solution(A):
    #A.sort()  # Add and delete
    #expect = [range(1,5)]
    sum2 = 0
    for item in A:
        sum2 += item       #or sum2 = sum(A)
    n = len(A)+ 1
    sum1 = n*(n+1)/2
    
    return int(sum1-sum2)

    
A = [] # Delete 

print(solution(A)) #Delete

# O(n)  O(1) Solution -- Alternatively we can loop over
