def GCD(a,b):
    f=min(a,b)
    g=max(b,a)
    m=0
    for i in range(1,f+1):
        if f%i==0 and g%i==0:
            m=i
    return m

# print(GCD(10,11))

def findTotient(a):
    m=0
    if a==1 or a==2:
        return 1

    for i in range(1,a):
        if GCD(a,i)==1:
            m=m+1
    return m

# print(findTotient(125))

def findNumbersWithTotientValue(f):
    l=[]
    for i in range(f*5):
        if(findTotient(i)==f):
            l.append(i)
    return l

m=int(input("enter the totient value : "))

f=findNumbersWithTotientValue(m)

print(f" All elements with totientValue of {m} are : \n {f}")
