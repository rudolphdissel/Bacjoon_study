#초기화
all_list=[]
all_ans_list=[]

#검사 함수
def check():
    c=0
    for x in range(5): #가로 빙고 검사.
        list_hap=0
        for y in range(5):
            list_hap+=all_list[x][y] 
        if list_hap==0:
            c+=1
    for x in range(5): #세로 빙고 검사
        list_hap=0
        for y in range(5):
            list_hap+=all_list[y][x]
        if list_hap==0:
            c+=1
    list_hap=0
    for x in range(5): #오른쪽 대각선 빙고검사
        list_hap+=all_list[x][x]
    if list_hap==0:
        c+=1
    list_hap=0
    for x in range(5):
        list_hap+=all_list[x][4-x]
    if list_hap==0:
        c+=1
    return c
#체크 함수
def ccount(n):
    for k in range(5): #플레이어가 쓴 숫자 위치를 찾아서 0으로 바꾼다.
        for l in range(5):
            if n==all_list[k][l]:
                all_list[k][l]=0


#입력 받기
for i in range(5):
    num_list=list(map(int,input().split()))
    all_list.append(num_list)

#정답판 받기.
for i in range(5):
    for j in list(map(int,input().split())):
        all_ans_list.append(j)

#검사시작
for i in range(25):
    ccount(all_ans_list[i]) #먼저 빙고 체크하기.
    if check()>=3: #한 번 3빙고뜨면 이제 확인 안 할거다
        print(i+1)
        break