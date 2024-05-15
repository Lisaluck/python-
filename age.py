print("**********calculaate your age****************")
a=int(input("enter the year of birth"))
try :
    a>1923 and  a< 2024
except Exception as e:
    print("invalid age")
print(" what you want to check ")
choices= [1]



if choices==1:
    
    print(" year in which the century be completed (100 years)")
    year=a+100
    print(year)
else:
    print("age in particular year ")
    b=int(input(" enter a year "))
    age=b-a
    print(age)
