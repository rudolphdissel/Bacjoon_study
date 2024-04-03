#input을 담기.
bracket = input()
length = len(bracket)
#stack에 하나씩 넣으면서 직전껄 확인하는 용도로 좋기에 stack
stack = []
tmp = 1
res = 0

#바구니에 있는거 다 꺼낼껀데
for i in range(length):
    b = bracket[i]   
    #열리는 괄호면 일단 x2축적시키고 스택에 넣어버린다.
    if b == '(':
        tmp *= 2
        stack.append(b)
    #마찬가지
    elif b == '[':
        tmp *= 3
        stack.append(b)
    #닫힐 때가 중요한데, 만약에 이상하게 닫히면 당연히 성립x
    elif b == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        #그건 아니라면, 직전것이 종속을 끝내는(?) 괄호인지 확인. 만약에 여기대로 '()'모양이라면 가장 안쪽의 종속이 끝난 모양새이다.
        if bracket[i-1] == '(':
            #그런 모양새라면 최종결과에 tmp를 담아내도된다. 
            res += tmp
        #tmp는 닫힌 만큼 원복시켜야 되는데, 그래야 바깥에 있는 괄호의 tmp만큼만 다시 결합된 괄호들에 영향을 준다. (곱셈의 분배법칙생각)
        tmp //= 2
        stack.pop() #하나의 괄호가 닫혔으면 꺼내버리기. 
    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if bracket[i-1] == '[':
            res += tmp
        tmp //= 3
        stack.pop() 
#이렇게 하다보면, tmp가 딱 맞는 값을 유지하면서 결합된 괄호들의 값을 더해가면서, 전체 bracket을 훑을 수 있따.
#stack에 값이 들어있다면 뭔가 괄호가 안 맞는것이므로 0.
if stack:
    res = 0
print(res)