n=int(input())

def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
    hanoi_tower(n-1, start, 6-start-end) 
    print(start, end)
    hanoi_tower(n-1, 6-start-end, end)

#하노이의 탑 이동횟수 공식
print(2**n-1)

if n<=20 :
    hanoi_tower(n,1,3)