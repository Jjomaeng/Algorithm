# 문제 : 한 번의 거래로 낼 수 있는 최대 이익을 산출하라

import timeit
 
start_time = timeit.default_timer() # 시작 시간 체크


input = [7,1,5,3,6,4]

def my_solution(input:list[int]) -> int:
    res = []
    for i in range(len(input)-1):
        res.append(-input[i]+max(input[i+1:]))
    print(res)
    return max(res)


#solution
import sys

def solution(prices:list[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price,price)
        profit = max(profit,price-min_price)
    return profit

print(solution(input))
terminate_time = timeit.default_timer() # 종료 시간 체크  
 
print("%f초 걸렸습니다." % (terminate_time - start_time)) 