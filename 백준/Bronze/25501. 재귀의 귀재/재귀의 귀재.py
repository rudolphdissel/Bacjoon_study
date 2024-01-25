def isPalindrome(s):
    return recursion(s, 0, len(s)-1,0)
def recursion(s, l, r,t):
    t+=1
    if l >= r: return 1, t
    elif s[l] != s[r]: return 0, t
    else: return recursion(s, l+1, r-1,t)


T=int(input())
for i in range(T):
    b=0
    s=input()
    a, b= isPalindrome(s)
    print(a,b)



