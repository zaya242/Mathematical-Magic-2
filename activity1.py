from math import sqrt
number=int(input("Enter your number \n"))
if number>1:
    for i in range(2,int(sqrt(number))+1):
        if(number%1==0):
            print(number, " is not prime")
            break
    else:
        print(number, " is prime")
else:
    print(number, " is not prime")
        
