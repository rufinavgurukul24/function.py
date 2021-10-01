#what is perfect number.

def checkperfect_number(num):
    num=int(input("Enter any number"))
    i=1 
    sum1 = 0
    while i<num:
        if num%i==0:
            sum1=sum1+i
            print(sum1)
    i=i+1 
    if sum1==num:
        print("The number is a Perfect number! ")
    else:
        print("The number is not a Perfect number!")
checkperfect_number()


