month_l = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
           'декабрь']

month = input("Введите месяц(строчно):")
day = int(input("Введите число(число):"))

for i in range(len(month_l)):
    if month_l[i] == month:
        nub_month = i+1

if ((nub_month == 3 and day >= 21) or (nub_month == 4 and day <= 20)):
    print("Овен")
elif((nub_month == 4 and day >= 21) or (nub_month == 5 and day <= 20)):
    print("Телец")
elif((nub_month == 5 and day >= 21) or (nub_month == 6 and day <= 20)):
    print("Близнецы")
elif((nub_month == 6 and day >= 21) or (nub_month == 7 and day <= 22)):
    print("Рак")
elif((nub_month == 7 and day >= 23) or (nub_month == 8 and day <= 22)):
    print("Лев")
elif((nub_month == 8 and day >= 23) or (nub_month == 9 and day <= 22)):
    print("Дева")
elif((nub_month == 9 and day >= 23) or (nub_month == 10 and day <= 22)):
    print("Весы")
elif((nub_month == 10 and day >= 23) or (nub_month == 11 and day <= 22)):
    print("Скорпион")
elif((nub_month == 11 and day >= 23) or (nub_month == 12 and day <= 21)):
    print("Стрелец")
elif((nub_month == 12 and day >= 22) or (nub_month == 1 and day <= 19)):
    print("Козерог")
elif((nub_month == 1 and day >= 20) or (nub_month == 2 and day <= 19)):
    print("Водолей")
elif((nub_month == 2 and day >= 20) or (nub_month == 3 and day <= 20)):
    print("Рыбы")