cash=int(input())
stock=list(map(int,input().split()))

def bnp(cash, stock):
    amount=0
    for i in stock:
        while i <=cash:
            cash-=i
            amount+=1
    return stock[-1]*amount+cash

def timing(cash,stock):
    amount=0
    badflow=0
    goodflow=0
    for i in range(len(stock)):
        if i==0:
            previous=stock[i]
        else:
            if previous>stock[i]:
                badflow+=1
                goodflow=0
            elif previous==stock[i]:
                badflow=0
                goodflow=0
            elif previous<stock[i]:
                goodflow+=1
                badflow=0
            if goodflow>=3:
                cash+= amount*stock[i]
                amount=0
            elif badflow>=3:
                while cash>=stock[i]:
                    cash-=stock[i]
                    amount+=1
            # print(goodflow)
        previous=stock[i]
    # print(amount)
    # print(cash)
    return amount*stock[-1]+cash
        
        
if bnp(cash,stock)==timing(cash,stock):
    print('SAMESAME')
elif bnp(cash,stock)>=timing(cash,stock):
    print('BNP')
else:
    print('TIMING')
            