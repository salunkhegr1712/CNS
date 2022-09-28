def gcd(a,b):
    f=max(a,b)
    g=min(a,b)
    m=0
    for i in range(1,g+1):
        if f%i==0 and g%i==0:
            m=i
    return m

# print(gcd(10,8))

def multiplicativeInverse(n,m):
    if gcd(n,m)!=1:
        return -1111111
    
    b=min(n,m)
    a=max(n,m)
    q=a//b
    r=a%b
    t1=0
    t2=1
    t=t1-t2*q       

    while (r!=0):
        a=b
        b=r
        r=t1
        t1=t2
        t2=t
        q=a//b
        r=a%b
        t=t1-t2*q
    
    if t2<0:
        t2=max(n,m)+t2
    return t2

n=23
m=26
a=multiplicativeInverse(n,m)
if a<0:
    a=m+a
print(f"multiplicative inverse  of {n} mod {m} : {multiplicativeInverse(n,m)}")