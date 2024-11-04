# Исользуя условия (if-else-elif), напишите все четные числа от 1 до 100

for num in range (1,101,1):
    if num %2==0 and num != 100:
        print(num)

    elif num == 100:
        print("наконец-то 100")

print ("\nPart 2")
#Используя шаги в range (третье значение т.е шаг), напишите нечетные числа от 1 до 100

for num in range (1,101,1):
    if num %2!=0 and num < 100:
        print("odd = ", num)




#Создайте 4 переменных с int, float, str и bool про КНИГУ

name = "Психолог в концлагере" #str
count_pages = 350 #int
rating = 9.7 # float
is_ebook = False #bool про КНИГУ