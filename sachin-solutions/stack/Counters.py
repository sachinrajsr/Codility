# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    counter = [0]*N
    start_line = 0
    max_counter = 0

    for i in A:
        x = i-1
        if i > N:
            start_line = max_counter

        elif counter[x] < start_line:
            counter[x] = start_line+1

        else:
            counter[x] += 1
        
        if i<= N and counter[x]>max_counter:
            max_counter = counter[x]
    
    for i in range(len(counter)):
        if counter[i] < start_line:
            counter[i] = start_line
    return counter         
        