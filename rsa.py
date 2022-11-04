# here i will write the code for the RSA algorithm code 

# problem statement for the assignment]

# Write a program to
# 1)check whether the given number is prime or not?
# 2)find GCD (Greatest Common Divisor) of given two numbers.
# 3)check whether given numbers are relatively prime or not?
# 4)find multiplicative inverse of given two numbers
# 5)implement RSA algorithm Compute the time required for encryption and decryption.

# first we will write a function to check that a number is prime or not 

import random 
import math
def isPrime(n):
    if n==1 or n==0:
        return False
    elif n==2:
        return True
    else:
        k=2
        while(k<=n//2):
            if(n%k==0):
                return False
            k+=1
        return True

# lets check that our function works or not 
# print(isPrime(3))

# now we will write the function to find gcd for two numbers 
def GCD(a,b):

    f=max(a,b)
    g=min(a,b)
    m=0

    for i in range(1,g+1):
        if f%i==0 and g%i==0:
            m=i
    return m

# so lets check that is gcd function GCD working or not 
# print(GCD(10,2))

# now we will write the function such that we will see that 2 numbers are relatively prime to each other
# or not and according to that we will return the answer 

def isRelativelyPrime(a,b):
    if GCD(a,b)==1:
        return True
    return False

# check that is isRelativelyPrime function is working or not 
# print(isRelativelyPrime(15,4))

# now we will write the code for finding the multiplicativeInverse of numbers 

# the problwm will look like 
# 1= n mod(m)

# the order in which we are passing is important 
def multiplicativeInverse(n,m):
   
    if GCD(n,m)!=1:
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

# lets check is this really works or not 
c=multiplicativeInverse(10,99)
# print(c)
# print((c*10)%91)

# function to find euler totient value 
def findTotient(a):
    m=0
    if a==1 or a==2:
        return 1

    for i in range(1,a):
        if GCD(a,i)==1:
            m=m+1
    return m


# first we will write all Notation and according to it we will 
# write the code for it 
# p and q are prime numbers 
# n=p*q 
# we have to take any e such that is should greater than 1 and less than (p-1) and (q-1)
# so now we have find d such that e*d=1 mod((p-1)*(q-1))
# and return all 4 values e d p and q and n

# now plaintext is pp and ciphertext is cc 
# cc=pp*e mod(n)
# pp= cc*d mod(n)

def rsaValues(p,q):
    phi=(p-1)*(q-1)
    l=[]
    k=2
    e=0
    zz=findTotient(p*q)
    print(zz)
    while(k<phi):
    # e must be co-prime to phi and
    # smaller than phi.
        if(GCD(k, phi) == 1):
            l.append(k)
        
        k+=1
    # print(l)
    g=(len(l)//2) -1
    e=l[random.randint(0,g)]
    k=2
    d=(k*phi + 1) / e
    return e,d

# print(multiplicativeInverse(10,46))
def rsaEncrypt(p,q):
    n=p*q
    e,d=rsaValues(p,q)
    p=int(input("enter your no o encrypt"))
    print("original msg is : ",p)
    c = pow(p, e)
    c = math.fmod(c, n)
    print("cipher text is : ",c)
    m = pow(c, d)
    m = math.fmod(m, n)
    print("decrypted msg is : ",m)
    return c,d

