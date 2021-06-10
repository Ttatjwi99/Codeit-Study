def solution(progresses, speeds):
    #일단 각각 며칠 걸리는 지 계산
    #비교해서 결론 내기
    hihi = []
    answer = []
    count = 0
    total = 1

    #날짜 계산부터_나누었을 때 나머지가 있을 경우 하루를 더 해주어야 함
    for i in range(len(progresses)):
        if 0 == (100-progresses[i])%speeds[i]:
            hihi.append((100-progresses[i])/speeds[i])
        else:
            hihi.append((100-progresses[i])//speeds[i] + 1)

    #위에서 걸리는 시간을 계산해놓은 리스트 hihi를 이용
    while count < len(hihi):
        if count+total == len(hihi):
            answer.append(total)
            break
        elif hihi[count] >= hihi[count+total]:
            total += 1
        elif hihi[count] < hihi[count+total]:
            answer.append(total)
            count += total
            total = 1

    return answer
