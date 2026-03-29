#factorial recursive

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("Enter a positive number"))
if n<0:
    print("factorial not defined")
else:
    f=factorial(n)
    print('factorial of ',n ,'is ',f)