n,s,r = map(int,input().split())
s_list=list(map(int,input().split()))
r_list=list(map(int,input().split()))

# 중복 제거
r_list=set(r_list)
s_list=set(s_list)
intersection = r_list.intersection(s_list)
r_list = r_list.difference(intersection)
s_list = s_list.difference(intersection)

r_list=list(r_list)
s_list=list(s_list)
# 본 로직
r_list.sort()
s_list.sort()
for i in r_list:
    tar1=i-1
    tar2=i+1
    for j in s_list:
        if j==tar1:
            s_list.remove(j)
            break
        elif j==tar2:
            s_list.remove(j)
            break
print(len(s_list))