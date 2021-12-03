# 문제 : 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라. 나눗셈을 하지 않고 O(n)에 풀이하라

input = [1,2,3,4]

def mul(x):
    res = 1
    for i in x:
        res *= i
    return res


def my_solution(input : list[int]) ->list[int]:
    res = []
    ans = []

    for i in range(len(input)):
        res.append((input[:i] + input[i+1:]))

    ans = list(map(mul,res))
    return ans

#solution : 

def solution(nums:list[int]) -> list[int]:
    out = []
    p =1

    for i in range(0,len(nums)):
        out.append(p)
        p = p *nums[i]
    p = 1
    for i in range(len(nums)-1,0-1,-1):
        out[i] = out[i]*p
        p = p*nums[i]
    return out

