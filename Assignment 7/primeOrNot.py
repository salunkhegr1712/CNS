# check whether the given number is prime or not?
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


p=eval(input("enter the number : "))
if(isPrime(p)):
    print(f"the number {p} is a prime number")
    exit(0)
print(f"the number {p} is not a prime number")