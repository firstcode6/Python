stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def max_ad(stats):
    max1 = 0
    v = list(stats.values())
    k = list(stats.keys())
    for value in v:
        if max1 < value:
            max1 = value

    return k[v.index(max1)]

m = max_ad(stats)
print(m)
