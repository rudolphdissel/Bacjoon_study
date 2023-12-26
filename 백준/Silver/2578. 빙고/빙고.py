all_list=[]
ans_count=0
bingo=0
ans=0
play=1
for i in range(5):
    num_list=list(map(int,input().split()))
    all_list.append(num_list)

for j in range(5):
    check_list=list(map(int,input().split()))
    bingo=0
    for m in range(5):
        bingo=0
        ans_count+=1
        for k in range(5): #플레이어가 쓴 숫자 위치를 찾아서 0으로 바꾼다.
            for l in range(5):
                if check_list[m]==all_list[k][l]:
                    all_list[k][l]=0
        for x in range(5): #0으로 다 바꿨다면, 검사시작. (0,0)(0,1),(0,2)(0,3)(0,4)더하기.그합이 0이라면, 1빙고
            list_hap=0
            for y in range(5):
                list_hap+=all_list[x][y] 
            if list_hap==0:
                bingo+=1
        for x in range(5):
            list_hap=0
            for y in range(5):
                list_hap+=all_list[y][x]
            if list_hap==0:
                bingo+=1
        list_hap=0
        for x in range(5):
            list_hap+=all_list[x][x]
        if list_hap==0:
            bingo+=1
        list_hap=0
        for x in range(5):
            list_hap+=all_list[x][4-x]
        if list_hap==0:
            bingo+=1
        if bingo>=3 and play==1:
            ans=ans_count
            play=0
        else:
            bingo=0
print(ans)
