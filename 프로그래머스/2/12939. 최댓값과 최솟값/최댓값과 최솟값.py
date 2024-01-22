def solution(s):
    a=list(map(int, s.split()))
    h=max(a)
    l=min(a)
    return f"{l} {h}"