def solution(s):
    stack=[]
    for i in s:
        if stack!=[] and stack[-1]=='(' and i==')':
            stack.pop()
        else:
            stack.append(i)
    return False if stack else True
            
            