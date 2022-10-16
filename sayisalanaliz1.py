import math
def f(x):
  return x**3-2*x**2-5
buyuksayi=4
kucuksayi=2
sayi1=f(kucuksayi)
sayi2=f(buyuksayi)
if sayi1 * sayi2 < 0:
 for i in range(1,5):
     c=(kucuksayi+buyuksayi)/2
     sayi3=f(c)
     if (sayi1+ sayi3<0):
         buyuksayi=c
         sayi2=sayi3
     else:
        kucuksayi=a
        sayi11=sayi3
print("c=",c)