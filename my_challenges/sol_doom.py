def solution(area):
    answer_list = []
    while area > 0:
        ss = int(area ** .5)
        sa = ss ** 2
        area -= answer_list.append(sa)
    return answer_list
