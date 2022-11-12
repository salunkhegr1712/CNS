# find multiplicative inverse of given two numbers 

# A*X=1 mod(m)
# we have A and m and we have to find X 

def multiplicaiveInverse(a,m):
    

    for i in range(1,m):
        if((a*i)%m==1):
            return i

    return -1


a=eval(input("enter first number : "))
m=eval(input("enter second number : "))
g=multiplicaiveInverse(a,m)
if g!=1:
    print(f"multiplicative inverse of {a}*X = 1 mod ({m}) is : {g}")
    exit(0)
print(f"{a} and {m} are not relatively prime to each other ")
# print(multiplicaiveInverse(a,m))