def solution(input):
    stack = []
    answer = 0
    for i in range(len(input)):
        if input[i] == '(':
            stack.append("(")

        else :
            stack.pop()
            if input[i-1] == '(':
                answer += len(stack)
            else:
                answer += 1


    return answer

print(solution("()(((()())(())()))(())"))
