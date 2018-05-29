#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].
def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        print(num)
print("Perfect numbers between 1 and 1000 are:")
for i in range(1,1001):
    perfect(i)
    
