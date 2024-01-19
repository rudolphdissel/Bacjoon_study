def solution(a, b):
    hap=0
    if a<=b:
        for i in range(a,b+1):
            hap+=i
    else:
        for i in range(b,a+1):
            hap+=i
    return hap