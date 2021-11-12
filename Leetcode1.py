# 문제 : 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

input = [2,7,11,15] 
target = 9

def TwoSum(input : list[int], target : int) -> list[int]:
    for i in range(len(input)):
        for j in range(i+1,len(input)):
            if (input[i] + input[j]) == target:
                return [i,j]


print(TwoSum(input,target))

#solution : in을 활용하여 가볍고 빠르게(brute-force 사용x)

def solution1(input:list[int],target : int) -> list[int]:
    for i,n in enumerate(input):
        complement = target -n
    
    if complement in input[i+1]:
        return input.index(n),input[i+1:].index(complement) + (i+1)

#solution : 시간복잡도 개선

def solution2(input:list[int],target : int) -> list[int]:
    nums_map = {}
    for i , num in enumerate(input):
        nums_map[num] = i

    for i,num in enumerate(input):
        if target - num in nums_map and i != nums_map[target - num] :
            return input.index(num),nums_map[target - num]

#solution : 조회 구조 개선 

def solution3(input:list[int],target : int) -> list[int]:
    nums_map = {}
    for i,num in enumerate(input):
        if target - num in nums_map:
            return [nums_map[target - num],i]
        nums_map[num] = i
 
# solution = 투 포인트 이용하여 성능 개선 #정렬된 input을 받는 가정

def solution4(input:list[int],target : int) -> list[int]:
    left,right = 0 , len(input) -1
    while not left == right:
        if input[left] + input[right] <target:
            left += 1
        elif input[left] + input[right] >target:
            right += 1
        else :
            return left,right





