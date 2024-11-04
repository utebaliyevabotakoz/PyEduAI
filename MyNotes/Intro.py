name = "Bota"
age = 22
height = 1.85
is_student = False
is_student = True


double_quote= "Bota"
single_quote ='Bota'
triple_quote='''Bo
ta
new line'''


a,b,c,d = 10,5,2,1

#! red comment


#  целочисленное деление  (//) - раздели и оставь целую часть
#  остаток от деления (%) - раздели и достань остаток от деления
#  Возведение в степень (**)


#? Сложение

prod_name = 'Lenovo '
descr = ' is a good brand'

product_sentence = prod_name+  descr
print (product_sentence)

#? Умножение

one_star="*"
ten_stars=one_star*10
print (ten_stars)

#? целочисленное деление

pizza_boxes=7
people=3

pizza_boxes_per_person = pizza_boxes // people
print (pizza_boxes_per_person)


#? остаток от деления
left_over_person = pizza_boxes%people
print (left_over_person)


#  Возведение в степень
print (3**4)



oranges = 4
apples = 4
bananas= 3

print (apples==bananas)
print (apples>bananas)
print (apples<bananas)
print (oranges!=apples)


is_shiny_today = True
do_i_have_money = False

will_i_go_outside = is_shiny_today and do_i_have_money

print (will_i_go_outside , "will_i_go_outside")


is_rainy_today = False
is_shyny_tomorrow = True
skolko_u_menya_est = 5
will_i_go_outside_today= (skolko_u_menya_est>3) and not (is_rainy_today)
print ("today " , will_i_go_outside_today)

will_i_go_outside_tomorrow= (skolko_u_menya_est>3) and (is_shyny_tomorrow)
print ("tomorrow " , will_i_go_outside_tomorrow)





day_time = "morning"
am_i_hungry = True

# if day_time == "morning":
#     #? если это УТРО
#     if am_i_hungry == True:
#         #? если это УТРО и если я ГОЛОДЕН
#         print('КУШАТЬ НАДАААА, завтракаем')
#     else:
#         #? если это УТРО, но я НЕ ГОЛОДЕН
#         print('Утро, но я не голоден')


if day_time == 'morning' and am_i_hungry == True:
    print('КУШАТЬ НАДАААА, завтракаем')
elif day_time == 'morning' and am_i_hungry != True:
    print('Утро, но я не голоден')

