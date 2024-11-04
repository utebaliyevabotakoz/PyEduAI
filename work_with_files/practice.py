def create_write_numberts_into_files():
    with open ("numbers.txt","w") as file:
        numbers=[10,20,30,40,50]
        for number in numbers:
            file.write(f"{number}\n")

create_write_numberts_into_files()



def read_numbers_and_calc():
    numbers=[]

    with open ("numbers.txt","r") as file:
        for line in file:
            number = int (line.strip()) #убирает пробелы в конце строки
            numbers.append(number)

    total = sum (numbers)
    average = total /len(numbers)
    maxi = max(numbers)

    print(f"summa = {total}")
    print(f"avg = {average}")
    print(f"maxi = {maxi}")


read_numbers_and_calc()
