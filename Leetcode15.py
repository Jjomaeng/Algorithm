# 문제 : 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라

input = [-1,0,1,2,-1,-4]

def find3element(n : list[int]) -> list[int]:
    n.sort()
    f,c,b = 0,0,len(n)-1
    ans = []
    for c in range(len(n)) :
        f ,b, = 0,len(n)-1
        
        while f < b :
            if f == c :
                f +=1
            if b == c:
                b -= 1
            if n[f] + n[c] + n[b] == 0:
                temp = [n[f],n[c],n[b]]
                temp.sort()
                if temp not in ans:
                    ans.append(temp)
                f += 1

            elif n[f] + n[c] + n[b] < 0 :
                f += 1
            else :
                b -= 1
    
    return ans


# brute-force : 타임 아웃 되는 경우

def solution1(nums : list[int]) -> list[list[int]] :
    results = []
    nums.sort()

    for i in range(len(nums)) - 2:
        if i >0  and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-1):
            if j > i + 1 and nums[j] == nums[j - 1] :
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] ==0:
                    results.append((nums[i],nums[j],nums[k]))
    
    return results

    # 중복된 값 넘어가는 코드 추가 (계산 시간 더 줄이기)

def solution2(nums:list[int]) -> list[list[int]]:
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left,right = i+1,len(nums) -1
        while left <right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0 :
                left += 1
            elif sum > 0:
                right -= 1
            else:

                results.append((nums[i],nums[left],nums[right]))

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right -1]:
                    right += 1
                left += 1 ## 이 부분 가져가기
                right -= 1

    return results



