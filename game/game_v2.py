"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    number = np.random.randint(1, 101)  # число рандомно загадали
    #print(f'загадали: {number}')

    count = 0
    i = 0
    while True:
        count += 1
        if 50 > number >= 1 :# последовательный перебор в диапазоне 1-50 до загаданного числа
            seach_number = 1 + i 
            i += 1 
            if seach_number == number:
                #print(f'отгадали: {number}, попыток: {count}')
                break  # выход из цикла если угадали
        else:# последовательный перебор в диапазоне 50-100 до загаданного числа
            seach_number = 50 + i 
            i += 1 
            if seach_number == number:
                #print(f'отгадали: {number}, попыток: {count}')
                break  # выход из цикла если угадали
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
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
