"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток 
    """
    print('Загадано число: ',number)
    count = 0
    lst_num = list(range(1, 101))

    while True:
        count += 1
        predict_number = int(np.mean(lst_num))
        print('Попытка: ', count, ', предпологаемое число: ', predict_number)
        half = round(int(len(lst_num))/2)
      #print('Половинная отсечка: ', half)
        
        if number == predict_number:
            print(f'отгадано число: {number}, попыток: {count}')
            break
        elif predict_number < number:
            lst_num = lst_num[half:]
            print(f'интервал поиска от {lst_num[0]}') 
        else:
            lst_num = lst_num[:half]
            print('интервал поиска до ',lst_num[-1]) 
        if len(lst_num) == 0:
            break

    return count
    

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for seach_number in random_array:
        count_ls.append(random_predict(seach_number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
