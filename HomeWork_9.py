import numpy as np
import scipy.stats as stats


# Даны значения величины заработной платы заемщиков банка (zp) и значения 
# их поведенческого кредитного скоринга (ks): 
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110]) 
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n=10

# Используя математические операции, посчитать коэффициенты линейной регрессии,
# приняв за X заработную плату (то есть, zp - признак), а за y - значения
# скорингового балла (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.
b1=(n * np.sum(zp*ks) - np.sum(zp) * np.sum(ks))/(n * np.sum(zp**2) - np.sum(zp)**2)
print(b1)
# 2.6205388824027653

b1=(np.mean(zp*ks) - np.mean(zp) * np.mean(ks))/(np.mean(zp**2) - np.mean(zp)**2)
print(b1)
# 2.620538882402765

b0 = np.mean(ks) - b1 * np.mean(zp)
print(b0)
# 444.1773573243596

y_pred = b0 + b1 * zp
print(y_pred)
# [535.89621821 562.10160703 942.07974498 968.2851338  548.99891262
#  627.61507909 585.68645697 837.25818968 758.64202321 732.43663439]

mse = ((ks-y_pred)**2).sum()/n
print(mse)

# Посчитать коэффициент линейной регрессии при заработной плате (zp),
# используя градиентный спуск (без intercept).

def Mse (B1, y = ks, x = zp, n = 10):
    return np.sum((b1 * x - y)**2)/n
alpha = 0.000001
B1=0.1
"""
for i in range (10):
    B1 -= alpha * (2/n) * np.sum((B1 * zp - ks)*zp)
    print('B1 = {}'.format(B1))
"""
for i in range (1300):
    B1 -= alpha * (2/n) * np.sum((B1 * zp - ks)*zp)
    if i % 25 == 0:
        print('iteranion = {i}, B1 = {B1}, mse = {mse}'.format(i = i, B1 = B1, mse = Mse(B1)))   

# Произвести вычисления как в пункте 2, но с вычислением intercept. 
# Учесть, что изменение коэффициентов должно производиться на каждом 
# шаге одновременно (то есть изменение одного коэффициента не должно влиять 
# на изменение другого во время одной итерации).