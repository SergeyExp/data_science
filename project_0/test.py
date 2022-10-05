#@title Текст заголовка по умолчанию
"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import statistics

def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток 
    """
    print(number)
    count = 0
    lst_num = list(range(1, 101))

    while True:
      count += 1
      predict_number = int(np.mean(lst_num))
      half = round(int(len(lst_num))/2)
      print(half)
      if number == predict_number:
        break
      elif predict_number < number:
        lst_num = lst_num[half:]  
      else:
        lst_num = lst_num[:half]
      if len(lst_num) == 0:
        break

    return count

print(random_predict())