import math

def moduloInverse(a, m):
    for x in range(1, m):
        if ((a*x) % m == 1):
            return x
    return None

def find_ed(toitent,n):
    l = [x for x in range(2, toitent) if math.gcd(toitent, x) == 1]
    print(l)
    if l!=[]:
        for i in l:
            d = moduloInverse(i,toitent)
            if d is not None and d!=i:
                return i,d
        print("Cant find e")
        return
    else:
        print("Cant find e")
        return

def isPrime(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True

p = int(input("Enter Prime number p: "))
q = int(input("Enter Prime number q: "))
 
if (isPrime(p) and isPrime(q)):
    n = p*q
    print("Value of n is ", n)

    plaintText = int(input("Enter number to be encrypted. Should be less than product of prime numbers ("+str(n)+"): "))
    if plaintText <n:
        
        e,d = find_ed((p-1)*(q-1),n)
        print("Euler Totient is ", (p-1)*(q-1))
        print("value of e and d is ", e , d)
        print("Generated Public Key pair: {"+str(e)+","+str(n)+"}")
        print("Geerated Private Key pair: {"+str(d)+","+str(n)+"}")
        cipherText = (plaintText**e)%n
        print("CipherText is (plaintText**e)%n i.e "+str(cipherText))
        dec = (cipherText**d)%n
        print("Decrypted cipherText is (cipherText**d)%n i.e "+str(dec))
    else:
        print("You entered a number greater than "+str(n))
else:
    print("Numbers aren't prime")