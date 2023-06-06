import numpy as np
import scipy.stats as stats

# Выбрать тест и проверить, есть  ли различия между выборками:
# 1) Даны две  независимые выборки. Не соблюдается условие нормальности
# x1  380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции

x_1 = np.array([380, 420, 290])
y_1 = np.array([140, 360, 200, 900])

print(stats.mannwhitneyu(x_1, y_1))
# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)
# Вывод: Нулевая гипотеза верна, различия существуют



# 2 ) Исследовалось влияние препарата на уровень давления пациентов.
# Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут. 
# Есть ли статистически значимые различия?
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150,  130, 135
# 3е измерение через 30 минут: 130, 130, 120, 130, 125

a_1 = np.array([150, 160, 165, 145, 155])
a_2 = np.array([140, 155, 150, 130, 135])
a_3 = np.array([130, 130, 120, 130, 125])

print(stats.friedmanchisquare(a_1,a_2,a_3))
# FriedmanchisquareResult(statistic=9.578947368421062, pvalue=0.00831683351100441)
# Вывод: нулевая гипотеза не верна, статистически значимые различия есть.



# 3) Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.

print(stats.wilcoxon(a_1, a_2))
# WilcoxonResult(statistic=0.0, pvalue=0.0625)
# Вывод: нулевая гипотеза верна, татистически значимых различий нет.



# 4) Даны 3 группы  учеников плавания. Сравнить результаты для спортсменов.
# В 1 группе время на дистанцию 50 м составляют:
# 56, 60, 62, 55, 71, 67, 59, 58, 64, 67
# Вторая группа: 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
# Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54

gr_1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
gr_2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
gr_3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

print(stats.kruskal(gr_1, gr_2, gr_3))
# KruskalResult(statistic=5.465564058257224, pvalue=0.06503809985904942)
# Вывод: сатистически значимых различий не выявлено

