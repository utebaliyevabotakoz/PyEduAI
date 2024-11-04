
#* Операторы -- действия над данными

#* Арифметические операторы 
#? сложение (+), вычитание (-), умножение (*), деление (/) 
#? Целочисленное деление (//) - раздели и оставь целую часть
#? Остаток от деления (%) - раздели и достань остаток деления
#? Возведение в степень (**)

#! В основном используются с числами (сложение и умножение)

#? Пример СЛОЖЕНИЯ (строков)
product_name = "Asus Vivobook 16x"
description = " has a 16-inch display, with 16GB RAM and i5-13th gen"

product_sentence = product_name + description

#? Пример УМНОЖЕНИЯ (строков)

one_star = "*"
ten_stars = one_star * 10

#? Пример Целостного Деления
pizza_boxes = 7
people = 3
pizza_boxes_per_person = pizza_boxes // people

#? Пример выведения Остатка от деления
leftover_piza_boxes = pizza_boxes % people
# print(leftover_piza_boxes)

pizza_boxes = 10
people = 5
leftover_piza_boxes = pizza_boxes % people 
pizza_boxes_per_person = pizza_boxes // people

#! Обычное деление (/) всегда возвращает Float (дробное число), даже если деление идет без остатка

#* Сравнительные Операторы -- сравниваем два значения
#? Равно (==): проверяет, равны ли два значения.
#? Не равно (!=): проверяет, не равны ли два значения.
#? Больше (>): проверяет, больше ли одно значение другого.
#? Меньше (<): проверяет, меньше ли одно значение другого.
#? Больше или равно (>=): проверяет, больше или равно ли одно значение другому.
#? Меньше или равно (<=): проверяет, меньше или равно ли одно значение другому.

oranges = 4
apples = 4
bananas = 3

# print(apples == bananas) # False
#print(apples > bananas) # True
apples < bananas 
# print(oranges >= apples)
oranges <= apples
# print(oranges != apples)



#* Логические Операторы -- допросники условии или сравнении, которые возвращают булевые значения
#? and - Правда ли оба условия? 
#? or - Правда ли хотя бы одно условие?
#? not - Правда ли, что это не так?

is_rainy_today = False
do_i_have_money = False

will_i_go_outside = (is_rainy_today) and (do_i_have_money)  #правда ли ОБА условия? Если да то всё выражение ИСТИНА, а если нет, то всё выражение ЛОЖЬ
# print(will_i_go_outside)

skolko_u_menya_est = 5

will_i_go_outside = (skolko_u_menya_est > 2) and  (not (is_rainy_today))
# print(will_i_go_outside)

print((apples == bananas) or (apples > bananas)) # правда ли Хотя бы ОДНО из условии

you_are_lying_bananas_are_less_than_apples =  not (bananas > apples) # правда что условие после меня НЕВЕРНОЕ (правда ли что после меня идет ложь)
