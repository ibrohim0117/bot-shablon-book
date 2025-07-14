import math
n = 8
l = []



if n == 1:
    print(True)

elif n == math.factorial(2) or n == math.factorial(3) or n == math.factorial(5):
    print(True)

else:
    for i in range(2, n):
        if n % i == 0:
            if i != 2 and i != 3 and i != 5:
                l.append(i)

    if len(l):
        print(False)
    else:
        print(True)