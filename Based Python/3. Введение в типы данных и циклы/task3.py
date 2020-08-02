geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def sort_city(new_list, city):
    value_list=[]
    for i in new_list:
        if list(i.values())[0][1]==city:
            value_list.append(i)
    return value_list

fly_r = sort_city(geo_logs, 'Россия')
for i in fly_r:
    print(i)