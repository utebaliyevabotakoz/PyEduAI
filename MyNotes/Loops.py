# ######## 1
# x=1
# while x<3:
#     print(x, end=', ')
#     x = x+1 # x+=1
# print("\nEnded loop ", x)
#
#
# ######### 2
# str ="Hello"
# for a in str:
#     print (a)
#
#
#
# ##### 3
# for a in range(str): # (0,1,2,3,4)
#     print (a)
#
#
# ##### 4
# l=len(str)
# for a in range(l): # (0,1,2,3,4)
#     print (str[a])



# ##### 5
# str1 ="Madiyar"
# l=len(str1) #5
# for a in range(2,l,2): # range (start_index, end_index, step)
#     print (str1[a])
#     #2,4,6


# ##### 6
# str1 ="Madiyar"
# l=len(str1) #5
# for a in range(l-1,2,-1): # range (start_index, end_index, step)
#     print (str1[a])
#     #2,4,6


##### 7
# x=5
# while x<=30:
#     if x==10:
#         x+=5
#         continue
#     print(x)
#     x+=5
# print("Loop ended")



##### 8
# x=5
# while x<=30:
#     while x<=15:
#         if x==10:
#             break
#         print("second loop",x)
#         x+=5
#     print("first loop",x)
#     x+=5
# print("Loop ended",x)




#########
# Task1
#
# str = "Congratulations"
# for i in str:
#     if i=="a":
#         continue
#     print(i, end = ', ')
#
# print("\nPart2")
#
# # Task2
#
# for i in range (len (str)):
#     if i==5 or i==7:
#         continue
#     print(str[i], end = ' + ')


#######
# x=30
#
# if x%3 == 0:
#     print("x / by 3")
#
# if x%2 == 0:
#     print("x / by 2")
#
# if x%2 != 0:
#     print("x is odd")
#
# if x%100 == 30:
#     print("very good")


######Home work


print("\nHome work")
print("\nTask1")
x=0
while x<100:
    if x%3 == 0 or x%5 == 0 or x % 7 == 0 or x % 9 == 0:
        print(x, end = ', ')
    x+=1


print("\nTask2")

##### Task2
str = "Congratulations"
dlina = len(str)
for i in range (dlina):
    if i%2!=0:
        continue
    print (str[i])


print("\nTask3")

y=1
a=0
b=0
c=0
while y<=1000:
    if y % 15 != 0:
        a+=y
    if y % 17 != 0:
        b += y
    if y % 25 != 0:
        c += y
    y += 1
print("summa ne 15 = ",a)
print("summa ne 17 = ", b)
print("summa ne 25 = ", c)

