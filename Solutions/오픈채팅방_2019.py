# 관리자 창 "[닉네임]님이 들어왔습니다." "[닉네임]님이 나갔습니다."
# 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다. / 채팅방에서 닉네임을 변경한다.
# 기존 메세지들도 닉네임 변경되면 다 변경된다.
# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
#

from collections import defaultdict


def solution(record):
    answer = []

    id_name = defaultdict(int)
    message = []

    for rec in record:
        trans_list = rec.split()
        if len(trans_list) == 3:
            action, uid, name = trans_list
            id_name[uid] = name
            if action == "Enter":
                message.append([uid, action])
        else:
            message.append([trans_list[1], trans_list[0]])
    # print(id_name)
    for mess in message:
        if mess[1] == "Enter":
            answer.append(f'{id_name[mess[0]]}님이 들어왔습니다.')
        else:
            answer.append(f'{id_name[mess[0]]}님이 나갔습니다.')
    # print(answer)
    return answer

"""
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
return = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
"""