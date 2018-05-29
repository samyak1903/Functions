#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power(a,b):
    if b==0:
        return 1
    else:
        return a*pow(a,b-1)
a=int(input("Enter the number"))
b=int(input("Enter its power"))
print("%d^%d=%d" %(a,b,power(a,b)))
