# 3번의 기회 / 기회 마다 0~10점 SDT 재곱으로 계싼
# * 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. # 해당 점수 마이너스
# * 첫 번째 나오면 그것만 2배

import re


def solution(dartResult):
    answer = 0

    score = [11, 11, 11]

    string_list = re.findall('([0-9]+[\D]+)', dartResult)
    count = 0
    for string in string_list:
        length = len(string)
        if string[1].isdigit():
            score[count] = int(string[0:2])
            if string[2] == 'D':
                score[count] = score[count] ** 2
            elif string[2] == 'T':
                score[count] = score[count] ** 3
            if length == 4:
                if string[3] == '#':
                    score[count] = -score[count]
                else:
                    if count == 0:
                        score[count] = score[count] * 2
                    else:
                        score[count - 1] = score[count - 1] * 2
                        score[count] = score[count] * 2
        else:
            score[count] = int(string[0])
            if string[1] == 'D':
                score[count] = score[count] ** 2
            elif string[1] == 'T':
                score[count] = score[count] ** 3
            if length == 3:
                if string[2] == '#':
                    score[count] = -score[count]
                else:
                    if count == 0:
                        score[count] = score[count] * 2
                    else:
                        score[count - 1] = score[count - 1] * 2
                        score[count] = score[count] * 2
        count += 1
    for i in score:
        answer += i

    return answer

"""
dartResult = "1S2D*3T" / return 37
dartResult = "1D2S#10S" / return 9
dartResult = "1D2S0T" / return 3
dartResult = "1S*2T*3S" / return 23
dartResult = "1D#2S*3S" / return 5
dartResult = "1T2D3D#" / return -4
dartResult = "1D2S3T*" / return 59
"""