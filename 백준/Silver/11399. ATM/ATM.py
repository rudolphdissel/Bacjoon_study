#입력받기
time=[]
time_sum=0
N=int(input())
time=list(map(int,input().split()))
time.sort() #오름차순으로 정렬해서 더한게 무조건 최솟값
for i in range(N):
    time_sum+=sum(time[0:i+1]) #슬라이싱 범위를 한개씩 늘려가면 누적합시키기.
print(time_sum)