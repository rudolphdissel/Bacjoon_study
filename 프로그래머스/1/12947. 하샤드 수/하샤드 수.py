def solution(x):
    hap=0
    x=str(x)
    for i in x:
        hap+=int(i)
    if int(x)%hap==0:
        return True
    else:
        return False