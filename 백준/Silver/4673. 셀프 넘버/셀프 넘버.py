no_self=[]
for i in range(1,10000):
    hap=i
    while i>0 :
        hap+=i%10
        i//=10
    if hap<10001:
        no_self.append(hap)
no_self=set(no_self)
no_self=list(no_self)


self=[x for x in range(1,10001)]

for j in range(len(no_self)):
    self.remove(no_self[j])
for k in self:
    print(k)
  