from cgitb import small


def sumaPatrate(n):

    sp = 0

    for i in range(1, n + 1):
        sp += sp + (i * i)

    return sp       


nr = int(input())

print(sumaPatrate(nr))
