# Задача 4. В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

n = 100
k = 2
purchased_ticket = 2
import numpy as np
from math import factorial
def combi(n,k):
  return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))
all_result = combi (n,k) # всего сочетаний
lucky_result  = combi (k, purchased_ticket)
ver_lucky_ticket = lucky_result / all_result
print("Вероятность того, что 2 приобретенных билета окажутся выигрышными:", ver_lucky_ticket)
