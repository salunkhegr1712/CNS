# a basic function which is used in order to find out the greatest common divisor 
# between two number and if gc of two numbers is 1 then the numbers are called as
# relatively prime to each other 

def gcd(a,b):
    f=max(a,b)
    g=min(a,b)
    m=0
    for i in range(1,g+1):
        if f%i==0 and g%i==0:
            m=i
    return m

# print(gcd(10,8))

# The function which use a tabular method to find the value of the multiplicativeInverse and
# with the use of this we can able find the modular multiplicativeInverse of form
# n mod(m)
# here we take n and m and then forth we arwe going to return the output 

def multiplicativeInverse(n,m):
    if gcd(n,m)!=1:
        return -1111111
    
    # so here i will explain how this algo is going to work 

    # find the minimum and the maximum Element from the  two numbers 
    b=min(n,m)
    a=max(n,m)
    # find quotient for that we will use integer division 
    q=a//b
    # find remainder
    r=a%b
    # as it is initial stage so the value of the t1 and t2 are by default 0 and 1 respectively
    t1=0
    t2=1

    # then we will find the t an which has formula of T= T1-Q*T2 
    t=t1-t2*q       

    # in while loop we will provide a stop condition and which is remainder = 0 and at that time 
    # whatever the value of t2 is will be multiplicativeInverse of that operation 
    while (r!=0):
        # so here the one iteration is over
        # so here first we shift all values like  
        # b--> a ; r-->b; t1-->r; t2-->t1; t --> t
        # and then we are going to find new value of a and r 
        a=b
        b=r
        r=t1
        t1=t2
        t2=t
        q=a//b
        r=a%b
        t=t1-t2*q
    
    # so if value is negative then just find value and get the multiplicative inverse 
    if t2<0:
        t2=m+t2
    return t2

n=23
m=26

print("-------------- Form n mod (m) --------------")
print("enter value of n and m below ")
n=eval(input("n : "))
m=eval(input("m : "))
print(f"multiplicative inverse  of {n} mod {m} : {multiplicativeInverse(n,m)}")
