def solution(seoul):
    j=0
    for i in seoul:
        if i=="Kim":
            answer=j
            break
        else:
            j+=1
            continue
    return f"김서방은 {answer}에 있다"