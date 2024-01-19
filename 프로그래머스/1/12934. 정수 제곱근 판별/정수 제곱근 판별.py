def solution(n):
    x=int(n**0.5)
    x=x**2
    print(x)
    print(n)
    if x==n:
        return ((n**0.5)+1)**2
    else:
        return -1