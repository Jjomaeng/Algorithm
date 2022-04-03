# 문제 : 신고 결과 받기

def solution(id_list, report, k):

    # id당 빈 스리트 담는 dict 생성
    id_dict={}
    id_dict_len = {}
    stop = []
    answer = [0 for i in range(len(id_list))]

    for id in id_list :
        id_dict[id] = []

    # report 추가

    for rep in report:
        id,r = rep.split()

        if id in id_dict[r]:
            continue
        else :
            id_dict[r].append(id)
    
    #개수 세기
    for id in id_dict:
       id_dict_len[id] = len(id_dict[id])
   
    # 정지 당하는 아이디 찾기
    stop = [i for i,value in id_dict_len.items() if value >= k ]
    
    # 정지 메일 받기

    for id in stop:
        mail = id_dict[id]

        for i in mail:
            idx = id_list.index(i)
            answer[idx] += 1
    return answer

def solution2(id_list, report, k):

    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

    
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
solution2(id_list,report,2)




