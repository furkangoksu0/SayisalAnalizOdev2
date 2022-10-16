import math


def f(x):
    return x ** 3 + 4 * x ** 2 - 10


buyuksayi = 2
kucuksayi = 1
sayi1 = f(kucuksayi)
sayi2 = f(buyuksayi)
if sayi1 * sayi2 < 0:
    for i in range(1, 19):
        c = (kucuksayi + buyuksayi) / 2
        sayi3 = f(c)
        if sayi1 * sayi3 < 0:
            buyuksayi = c
            sayi2 = sayi3
        else:
            kucuksayi = c
            sayi1 = sayi3
print("c=", c)
