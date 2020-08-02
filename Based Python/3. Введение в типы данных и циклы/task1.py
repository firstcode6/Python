# Задача №1

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha', 'Lady']

if (len(boys) != len(girls)):
    print("Списки не равны, кто-то может остаться без пары!")
else:
    boys_sort = sorted(boys)
    girls_sort = sorted(girls)
    print("Идеальные пары:")
    for i, j in zip(boys_sort, girls_sort):
        print(i + " и " + j)
