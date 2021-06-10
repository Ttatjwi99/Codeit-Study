#첫 번째 방법
#하나하나 비교해보면서 없는 이름을 answer로
def solution(participant, completion):
    gil2 = len(participant)
    count = 0
    
    for i in range(gil2-1):
        while count <= len(participant):
            if len(completion) == 1:
                answer = participant[count]
                return answer
            elif participant[count] == completion[i]:
                del participant[count]
                count = 0
                break
            elif participant[count] != completion[i]:
                count += 1
                
                
                
                
#정렬을 해서 두 개를 비교해보자
def solution(participant, completion):
    ptc = sorted(participant)
    cpt = sorted(completion)
    gil2 = len(ptc)
    count = 0

    while count < gil2:
        #리스트 끝까지 갔을 때
        if count == gil2-1:
            answer = ptc[count]
            return answer
        #참가자와 완주한 사람이 같을 때
        elif ptc[count] == cpt[count]:
            count += 1
        #참가자와 완주한 사람이 다를 때
        else:
            answer = ptc[count]
            return answer
