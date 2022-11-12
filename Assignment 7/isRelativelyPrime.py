# check whether given numbers are relatively prime or not? 
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

a=eval(input("enter first number : "))
b=eval(input("enter second number : "))

if(relativelyPrime(a,b)):
    print(f"the numbers {a} and {b} are relatively prime to each other")
    exit(0)
print(f"the numbers {a} and {b} are not relatively prime to each other")
