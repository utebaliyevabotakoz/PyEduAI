
#? 1) Зачем нам нужны условия?
#? 2) Зачем нужны elif? else?
#? 3) Исходя из урока об операторах (первый урок), какие операторы можно использовать, чтобы укоротить следующий код?:

day_time = "morning"
am_i_hungry = True

if day_time == "morning":
    #? если это УТРО
    if am_i_hungry == True:
        #? если это УТРО и если я ГОЛОДЕН
        print('КУШАТЬ НАДАААА, завтракаем')
    else:
        #? если это УТРО, но я НЕ ГОЛОДЕН
        print('Утро, но я не голоден')

if (day_time == ' morning') and (am_i_hungry == True):
    print('asdf')


