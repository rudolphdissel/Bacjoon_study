def solution(s):
    answer = True
    s=s.upper()
    for i in s:
        pcount=s.count("P")
        ycount=s.count("Y")
    if pcount==ycount:
        answer=True
    else:
        answer=False
    

    

    return answer