import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# Провести дисперсионный анализ для определения того, есть ли различия среднего роста
# среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

y1 = np.array([173, 175, 180, 178, 177, 185, 183, 182])
y2 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
y3 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

k = 3
n = 28

# Средние значения выборок 1, 2, 3 
y_mean_1 = np.mean(y1)
print(y_mean_1)

y_mean_2 = np.mean(y2)
print(y_mean_2)

y_mean_3 = np.mean(y3)
print(y_mean_3)

# Определение среднего значения по всем выборкам
total = np.concatenate([y1, y2, y3])
print(total)

y_mean_total = np.mean(total)
print(y_mean_total)

# сумма квадратов отклонений наблюдений от общего среднего
print(np.sum((total - y_mean_total)**2))

# Сумма квадратов отклонений средних групповых значений от общего среднего
S_f = (np.sum((y_mean_1 - y_mean_total)**2) * 8 + 
       np.sum((y_mean_2 - y_mean_total)**2) * 9 + 
       np.sum((y_mean_3 - y_mean_total)**2) * 11)
print(S_f)

# Остаточная сумма квадратов отклонений
S_ost = (np.sum((y1 - y_mean_1)**2)+
         np.sum((y2 - y_mean_2)**2)+
         np.sum((y3 - y_mean_3)**2))
print(S_ost)

print(S_f + S_ost)

# Расчет факторной дисперсии
D_f = S_f / (k - 1)
print(D_f)

# Расчет остаточной дисперсии
D_ost = S_ost / (n - k)
print(D_ost)

# Расчет критерия Фишера
F_n = D_f / D_ost
print(F_n)

f = stats.f_oneway(y1, y2, y3)
print(f)

# F_onewayResult(statistic=5.500053450812596, pvaЮlue=0.010482206918698693)
# Вывод: выявлены статистически значимые различия, гипотеза о влиянии 
# вида спорта на средний рост спортсменов верна.

from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

df = pd.DataFrame({'score':[173, 175, 180, 178, 177, 185, 183, 182,
                            177, 179, 180, 188, 177, 172, 171, 184, 180, 
                            172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170],
                    'group': np.repeat(['Футболисты', 'хокеисты', 'штангисты'], repeats=([8, 9, 11]))})
tukey = pairwise_tukeyhsd(endog=df['score'],
                          groups=df['group'],
                          alpha=0.05)
print(tukey)

# Вывод: выявлены статистически значимые различия в группах фтболисты-штангисты 
# и хокеисты-штангисты
