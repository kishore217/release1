from ast import operator


a=input ("Enter 1st Value : ")
operator = input("Enter Operator as +,-,*,/ :" )
b=input ("Enter 2nd Value : ")

a=int (a)
b= int (b)

if operator == "+":
    print (a+b)
elif operator == "-":
    print (a-b)
elif operator == "*":
    print (a*b)
elif operator == "/":
    print (a/b)
else:
    print ("Wrong Operator")