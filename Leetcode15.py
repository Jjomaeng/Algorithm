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

print(find3element(input))
