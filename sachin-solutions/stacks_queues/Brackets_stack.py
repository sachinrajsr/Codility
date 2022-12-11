
def solution(S):
    valid = True
    stack = []
    for i in S:
        if i == "{" or i == "[" or i == "(":
            stack.append(i)
        elif i == "]":
            valid = False if not stack or stack.pop() != "[" else valid
        elif i == "}":
            valid = False if not stack or stack.pop() != "{" else valid
        elif i == ")":
            valid = False if not stack or stack.pop() != "(" else valid

    return 1 if valid and not stack else 0