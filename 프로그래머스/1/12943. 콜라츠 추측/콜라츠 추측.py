def solution(num):
    count_num=0
    while num!=1:
        if num%2==0:
            num/=2
        else:
            num=num*3+1    
        count_num+=1
        if count_num==500:
            return -1
    return count_num