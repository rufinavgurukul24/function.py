#leap year program.............



def checkYear(year):
    
     import calendar
     return(calendar.isleap(year))
     
year=int(input("enter the last year"))
i=1
while i<=year:
    if i%4==0:
        print(i,"Leap Year")
    else:
        print("normal year")
    i=i+1
checkYear(year)   
