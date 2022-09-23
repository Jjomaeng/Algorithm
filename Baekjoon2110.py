def conut_router(dist,house):
    cnt = 1
    pos = house[0]

    for next_pos in house:
        if next_pos - pos >= dist:
            cnt += 1
            post = next_pos
    return cnt

def get_upper_bound(left,right,target,house) :
    while left <= right:
        mid = (left + right) // 2
        installed = conut_router(mid,house)

        if installed >= target:
            left += mid + 1
        else :
            right = mid -1
    return left

def solution(n,c,house):
    house.sort()

    return get_upper_bound(1,house[n-1] - house[0],c,house) - 1