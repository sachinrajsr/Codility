
def solution(X, Y, D):
    goal = Y-X
    full_jump = goal // D
    small_jump = 1 if goal % D > 0 else 0
    return small_jump+full_jump