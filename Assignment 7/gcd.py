# find GCD (Greatest Common Divisor) of given two numbers.

def GCD(a,b):
    
    f=max(a,b)
    g=min(a,b)
    m=0

    for i in range(1,g+1):
        if f%i==0 and g%i==0:
            m=i
    return m

a=eval(input("enter first number : "))
b=eval(input("enter second number : "))

print(f" gcd of {a} and {b} is : {GCD(a,b)}")