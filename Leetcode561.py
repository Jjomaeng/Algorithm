#문제 : n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

input = [1,4,3,2,5,6]

def arrayPartition(n) :
    n.sort()
    list_min = min(n.pop(), n.pop())
    if len(n) > 2:
        list_min += arrayPartition(n)
        return list_min
    else :
        list_min += min(n.pop(), n.pop())
        return  list_min

print(arrayPartition(input))

#solution 1 : 재귀 쓰지 않기

def solution1(nums:list[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum

#solution 2: 짝수 값 이용

def solution2(nums:list[int]) -> int:
    sum = 0
    nums.sort()

    for i ,n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    return sum

# solutin3 : 슬라이싱 최적화

def solution3(nums:list[int]) -> int:
    return sum(sorted(nums)[::2])