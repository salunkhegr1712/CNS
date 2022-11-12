# implement RSA algorithm Compute the time required for encryption and decryption. 
import time
# check whether given numbers are relatively prime or not? 
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


def GCD(a,b):
    
    f=max(a,b)
    g=min(a,b)
    m=0

    for i in range(1,g+1):
        if f%i==0 and g%i==0:
            m=i
    return m

def relativelyPrime(a,b):
    if(GCD(a,b)==1):
        return True
    return False

def multiplicaiveInverse(a,m):
    for i in range(1,m):
        if((a*i)%m==1):
            return i
    
    return -1

def findKeys(p,q):
    t=(p-1)*(q-1)
    n=p*q
    l=[]
    for i in range(2,t):
        if(GCD(i,t)==1):
            l.append(i)
    # print(l)
    if l!=[]:
        for e in l:
            d = multiplicaiveInverse(e,t)
            if d!=-1 and d!=i:
                return e,d

        print("Cant find e")
        return
    else:
        print("Cant find e")
        return

# print(findKeys(11,13))

p = int(input("Enter Prime number p: "))
q = int(input("Enter Prime number q: "))

if(isPrime(p) and isPrime(q)):
    n=p*q
    t=(p-1)*(q-1)
    pp=eval(input(f"enter number such that number should less than {p*q} : "))
    if pp < n:
        encryptionStartTime=time.time()
        e,d=findKeys(p,q)
        print(f"plaintext is : {pp}")
        print(f"public Key pair: {e} and {n}")
        print(f"private Key pair: {d} and {n}")
        cc = (pp**e)%n
        print(f"ciphertext is : {cc}")
        encryptionEndTime=time.time()
        
        dp = (cc**d)%n
        print(f"decrypted msg is : {dp}")
        decryptionEndTime=time.time()

        print(f"total time for encryption is {encryptionEndTime-encryptionStartTime}")
        print(f"total time for decryption is {decryptionEndTime-encryptionEndTime}")
    else:
        print(f"entered a number greater than {n}")
else:
    print("entered number aren't prime")