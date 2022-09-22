def solution(id_list, report, k):
    answer = []
    # 신고가 k번 이상 당한 사람 찾기
    # 초기화
    reported_list = []
    reporter_list = []
    for i in range(len(id_list)):
        reported_list.append([])
        reporter_list.append([])
        answer.append(0)
    for every_report in report:
        reporter, reported = map(str, every_report.split(' '))
        index = id_list.index(reported)
        index_2 = id_list.index(reporter)
        if reporter not in reported_list[index]:
            reported_list[index].append(reporter)
        if reported not in reporter_list[index_2]:
            reporter_list[index_2].append(reported)
    # print(reported_list)
    # print(reporter_list)
    email_reported = []
    for j in range(len(reported_list)):
        if len(reported_list[j]) >= k:
            email_reported.append(id_list[j])
    # print(email_reported)
    for k in range(len(reported_list)):
        for every_person in email_reported:
            if every_person in reporter_list[k]:
                answer[k] = answer[k] + 1
    """
    print("id_list is : ", id_list)
    print("email_reported : ", email_reported)
    print("reported_list : ", reported_list)
    print("reporter_list : ", reporter_list)
    """
    return answer

"""
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
return = [2,1,1,0]

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
return = [0, 0]
"""