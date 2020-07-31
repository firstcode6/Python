print("Шоколадка имеет вид прямоугольника, разделенного на n×m долек.")
n = int(input("n="))
m = int(input("m="))
k = int(input("k="))

if ((k < n * m) and (k % n == 0) or (k % m == 0)):
    print("Yes")
else:
    print("No")
