# Задача 2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно.
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

n = 10
k = 3
import numpy as np
from math import factorial
def combi(n,k):
  return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))
all_result = combi (n,k)
result = 1 / all_result
print("Вероятность, что человек, не знающий код, откроет дверь с первой попытки", result)
