# Задача 1. Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все карты – крести. б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

import numpy as np
from math import factorial
def combi(n,k):
  return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))
all_result = combi (52,4) # всего сочетаний
print("Всего сочетаний в колоде:", all_result)
cresti_result = combi (13,4) # всего сочетаний по крести
print("Всего сочетаний по крести:", cresti_result)
ver_cresti = cresti_result / all_result
print("Вероятность, что все карты крести:", ver_cresti)
ace_result = combi (4,1) * combi (48,3) + combi (4,2) * combi (48,2) + combi (4,3) * combi (48,1) + combi (4,4) * combi (48,0) # всего сочетаний по тузам
ver_ace = ace_result / all_result
print("Вероятность, что в выбранных картах хотя бы 1 туз:", ver_ace)
