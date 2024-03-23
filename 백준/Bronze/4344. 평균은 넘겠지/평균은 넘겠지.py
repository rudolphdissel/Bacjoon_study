#case 갯수 입력받기
c=int(input())

#케이스 입력 값 만큼 반복
for i in range(c):
    count=0
    score_list=list(map(int,input().split()))
    #학생명수 추출
    student_n=score_list[0]
    #평균 점수
    avg=sum(score_list[1:])/student_n
    #평균 넘는 사람 세기
    for j in range(1,student_n+1):
        if score_list[j]>avg:
            count+=1
    #평균 넘는 사람비율 계산
    print("{:.3f}%".format(count/student_n*100))
            
    