#Q.3- Print multiplication table of 12 using recursion.
i=1
def mul(n,i):
    if i>10:
        return 0
    else:
        print("%d * %d = %d" %(n,i,n*i))
        mul(n,i+1)
num=int(input("Enter the number"))
mul(num,i)
