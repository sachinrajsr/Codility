# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")

# # O(N^2) with memory leak
# def solution(X, A):
#     path = []
#     index = 0
#     for i in range(len(A)):
#         if A[i] not in path:
#             path.append(A[i])
#             index
#         if sum(path) == X*(X+1)/2:
#                 return i
#     else:
#         return -1
        
# #Soln O(n2) with memory leak
# def solution(X, A):
#     path = list(range(1,X+1))
#     index = 0 
#     for i in range(len(A)):
#         if A[i] in path:
#             path.remove(A[i])
#             index = i
#     if len(path) == 0:
#         return index
#     else:
#         return -1

# print(solution(5, [1, 3, 1, 4, 5, 2, 5, 4]))




def solution(X, A):
    river_position = [False]*(X+1)
    for time in range(len(A)):
        pos = A[time]
        if not river_position[pos]:
            river_position[pos] = True
            X -= 1
            if X == 0:
                return time
    else: return -1


def solution(X, A):
    river_position = ["empty"]*(X+1)
    for time in range(len(A)):
        pos = A[time]
        if river_position[pos] != "leaf":
            river_position[pos] = "leaf"
            X -= 1
            if X == 0:
                return time
    else: return -1
        
        