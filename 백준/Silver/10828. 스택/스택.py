#스택.

#새로 배운 점.
#list에 pop 메서드를 쓰면 제일 오른쪽 요소가 제거된다.

import sys
n= int(sys.stdin.readline())
stack=[]
for i in range(n):
    in_value= sys.stdin.readline().split()
    #push 명령어가 들어왔다면
    if len(in_value)==2:
        stack.append(in_value[1])
    else:
        in_value=in_value[0]
        if in_value=="top":
            if stack==[]:
                print(-1)
            else: 
                print(stack[len(stack)-1])
        elif in_value=="size":
            print(len(stack))
        elif in_value=="empty":
            if stack==[]:
                print(1)
            else: 
                print(0)
        elif in_value=='pop':
            if stack==[]:
                print(-1)
            else:
                print(stack[-1])
                # stack=stack[:-1]
                stack.pop()
            
            

        
    
