from datetime import datetime
from idlelib.iomenu import encoding



def divide_numbers():
    try:
        num = int (input("Vvedite chislo "))
        divide_10 = 10/num
        print ("result = ", divide_10)
    except ZeroDivisionError:
        print("Impossible division by 0 ")
    except ValueError:
        print("Impossible symbol ")
    print("WE live even after errors ")

# divide_numbers()



def read_files (file_path):
    try:
        with open (file_path, "r", encoding="utf-8") as file:
            content = file.read()  # чтение содержимого файла
            print("содержиммое перед записью ", content)

    except FileNotFoundError:
        print ("файл не найден")

    except PermissionError:
        print("Недостаточно прав для открытия")

    except Exception as error :
        print( f"есть ошибка {error} ")

    finally:
        print("Завершение работы функцио ")


# read_files ("examples.txt")



import random, datetime, string

def get_passsword_len():
    while True:
        try:
            password_len = int(input ("vvedite dlinu ot 6-16 symbols\n"))
            if (password_len >= 6) and (password_len <= 16):
                return password_len
            else:
                print("Vvedite dlinu ot 6 do 16 ")
        except ValueError:
            print ("Error: Type number type")


# get_passsword_len()



def is_special_symbol():
    is_there_symbol = input("Do you want to add special symbols (yes/No)?\n")
    if is_there_symbol.lower() =="yes":
        return True
    else:
        return False

# is_special_symbol()



def generate_password(pass_len, is_special_symbol):
    string_of_all_elements = string.ascii_letters + string.digits

    if is_special_symbol:
        string_of_all_elements += string.punctuation

    password = ''

    for element in range (pass_len):
        password += random.choice(string_of_all_elements)

    return password




# password = generate_password (7, True)
# print (password)



def save_password(password):
    want_to_save = input ("Do you want to save password? (yes/no) \n")

    if want_to_save.lower() =="yes":

        website = input ("Which platform do you want to use this password for? \n")
        date_now = datetime.datetime.now()
        nice_date_now = datetime.datetime.strftime( date_now , "%d/%m/%Y, %H:%M:%S")

        with open ("gnrt_pswrd.txt", 'a', encoding = 'utf-8') as file:

            file.write(f'{website} ---- {password} --- {str (nice_date_now)} \n')
    else:
        print ("ok, do not forget! :) ")
        return


    print("Successfully saved!!!")

    return


def main ():
    password_len = get_passsword_len()
    any_symbols = is_special_symbol()
    final_password = generate_password(password_len, any_symbols)
    save_password(final_password)

main()
