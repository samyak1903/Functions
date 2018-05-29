#Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary
d={}
choice='y'
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
while choice.lower()=='y':
    num=int(input("Enter the number whose factorial has to be calculated: "))
    factorial=fact(num)
    d[num]=factorial
    print(d)
    choice=input("Want to enter more: y/n ")
