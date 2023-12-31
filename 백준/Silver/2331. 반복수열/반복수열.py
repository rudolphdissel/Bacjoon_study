#입력받기
A,P=map(int,input().split())
num_list=[A]

#연산 수행 함수.
def repeat_num(num):
    new_num=0
    #연산을 위한 for문
    for i in str(num):
        new_num+=int(i)**P
    #결과물 리스트에 담기.
    num_list.append(new_num)
    #이전에 나왔던 값인지 확인
    if num_list.count(new_num)==2:
        check=new_num
        ans=0
        #그 값이 몇 번째에 나왔던 값인지 확인해서, 답을 출력.
        for j in num_list:
            ans+=1
            if j==check:
                ans-=1
                print(ans)
                break
    #만약 아직 반복이 이루어 지지 않았다면 새로운 숫자로 다시 함수 반복
    else:
        repeat_num(new_num)
repeat_num(A)
