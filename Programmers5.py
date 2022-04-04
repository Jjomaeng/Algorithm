#문제 : 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    count = 0
    win = 0
    for lotto in lottos:
        if lotto == 0:
            count += 1
        elif lotto in win_nums:
            win += 1
            win_nums.remove(lotto)
    if len(win_nums) > count :
        max_win = 7-count-win
    else :
        max_win = 7-len(win_nums) -win

    if win == 0 :
        low_win = 6
    else :
        low_win = 7 - win
    answer = [max_win,low_win]
    return answer

def solution2(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

lottos = [45, 4, 35, 20, 3, 9]

win_nums = [46, 5, 36, 21, 4, 10]

print(solution(lottos,win_nums))