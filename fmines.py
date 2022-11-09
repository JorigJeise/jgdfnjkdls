import random
import numpy as np

def fmines():
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([1, 2, 3, 4, 5])
    array3 = np.array([1, 2, 3, 4, 5])
    array4 = np.array([1, 2, 3, 4, 5])
    array5 = np.array([1, 2, 3, 4, 5])

    row = random.randint(1, 5)

    if row == 1:
        num = random.randint(1, 5)
        array1 = str(array1).replace(str(num), ":white_check_mark:")

    elif row == 2:
        num = random.randint(1, 5)
        array2 = str(array2).replace(str(num), ":white_check_mark:")

    elif row == 3:
        num = random.randint(1, 5)
        array3 = str(array3).replace(str(num), ":white_check_mark:")

    elif row == 4:
        num = random.randint(1, 5)
        array4 = str(array4).replace(str(num), ":white_check_mark:")

    elif row == 5:
        num = random.randint(1, 5)
        array5 = str(array5).replace(str(num), ":white_check_mark:")


    for i in range(5):
        row = random.randint(1, 25)

        if row == 1:
            num = random.randint(1, 5)
            array1 = str(array1).replace(str(num), ":white_check_mark:")

        elif row == 2:
            num = random.randint(1, 5)
            array2 = str(array2).replace(str(num), ":white_check_mark:")

        elif row == 3:
            num = random.randint(1, 5)
            array3 = str(array3).replace(str(num), ":white_check_mark:")

        elif row == 4:
            num = random.randint(1, 5)
            array4 = str(array4).replace(str(num), ":white_check_mark:")

        elif row == 5:
            num = random.randint(1, 5)
            array5 = str(array5).replace(str(num), ":white_check_mark:")

    array1 = str(array1).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:').replace(str(4), ':question:').replace(str(5), ':question:')
    array2 = str(array2).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:').replace(str(4), ':question:').replace(str(5), ':question:')
    array3 = str(array3).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:').replace(str(4), ':question:').replace(str(5), ':question:')
    array4 = str(array4).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:').replace(str(4), ':question:').replace(str(5), ':question:')
    array5 = str(array5).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:').replace(str(4), ':question:').replace(str(5), ':question:')

    array1 = str(array1).replace(' [', '').replace('[','').replace(']', '')
    array2 = str(array2).replace(' [', '').replace('[','').replace(']', '')
    array3 = str(array3).replace(' [', '').replace('[','').replace(']', '')
    array4 = str(array4).replace(' [', '').replace('[','').replace(']', '')
    array5 = str(array5).replace(' [', '').replace('[','').replace(']', '')

    return f"{array1}\n{array2}\n{array3}\n{array4}\n{array5}"