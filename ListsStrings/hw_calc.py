num1 = int (input("enter your 1st num "))

act = input("enter your operation ")

num2 = int (input("enter your 2nd num "))
if num2==0:
    print ("2nd num can't be 0")
    num2=1

if act=='+':
    print (num1+num2)
elif act=='-':
    print (num1-num2)
elif  act=='*':
    print (num1*num2)
elif act=='/':
    print (num1/num2)