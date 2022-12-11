def solution(A):
    stack = []
    for i in A:
        if not stack:
            stack.append(i)
        else:
            x = stack[-1]
            if stack[-1] == i:
                stack.append(i)
            else:
                stack.pop(-1)
    occurances = A.count(stack[0])
    half_size = (len(A))/2
    if occurances > half_size:
        return A.index(stack[0])
    else: 
        return -1    


###########VS############ better way >>



def solution(A):
    lead_count = 0
    current_leader = 0
    for i in A:
        if lead_count == 0:
            current_leader = i
            lead_count += 1
        elif current_leader == i:
            lead_count += 1
        else:
            lead_count -= 1
    occurances = A.count(current_leader)
    half_size = (len(A))/2
    if occurances > half_size:
        return A.index(current_leader)
    else: 
        return -1    