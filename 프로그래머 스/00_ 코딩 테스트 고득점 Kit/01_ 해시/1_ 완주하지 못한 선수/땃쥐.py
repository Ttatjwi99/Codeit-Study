#정렬을 해서 두 개를 비교해보자
def solution(participant, completion):
    ptc = sorted(participant)
    cpt = sorted(completion)
    gil2 = len(ptc)
    count = 0

    while count < gil2:
        if count == gil2-1:
            answer = ptc[count]
            return answer
            break
        elif ptc[count] == cpt[count]:
            count += 1
        else:
            answer = ptc[count]
            return answer
            break
