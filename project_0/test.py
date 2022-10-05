    if predict_number >= 50:
        number = np.random.randint(50, 101)
        while True:
            count += 1
            if number == predict_number:
                print(f'отгадали: {number}, попыток: {count}')
                break  # выход из цикла если угадали
        return count 
    else:
        number = np.random.randint(1, 50)   
        while True:
            count += 1
            if number == predict_number:
                print(f'отгадали: {number}, попыток: {count}')
                break  # выход из цикла если угадали
        #print(f'отгадали: {number}') 
        return count    