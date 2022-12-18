# Задача 3. В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

n = 15
k = 9
detail = 3
import numpy as np
from math import factorial
def combi(n,k):
  return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))
all_result = combi (n,k) # всего сочетаний
print("Всего сочетаний деталей:", all_result)
paint_result = combi (k,detail) # всего сочетаний по окрашенным
print("Всего сочетаний по окрашенным:", paint_result)
ver_paint = paint_result / all_result
print("Вероятность, что все детали окрашены:", ver_paint)
