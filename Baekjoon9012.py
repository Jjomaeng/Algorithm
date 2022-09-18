def solution(T,inputs):
    answer = []
    for i in range(T):
        stack = []
        flag = True
        for c in inputs[i]:
            if c == '(':
                stack.append('(')
            else:
                if(len(stack) > 0):
                    stack.pop()
                else:
                    flag = False
                    break
        if flag and len(stack) == 0:
            answer.append('YES')
        else:
            answer.append('NO')

    return answer 

T = 3
inputs = ['(())()','(((()())()','()()']
print(solution(T,inputs))