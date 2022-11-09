import random
import numpy as np

def ptowers():
    array1 = np.array([1, 2, 3])
    array2 = np.array([1, 2, 3]) 
    array3 = np.array([1, 2, 3]) 
    array4 = np.array([1, 2, 3]) 
    array5 = np.array([1, 2, 3]) 
    array6 = np.array([1, 2, 3]) 
    array7 = np.array([1, 2, 3]) 
    array8 = np.array([1, 2, 3]) 

    num = random.randint(1, 3)
    array1 = str(array1).replace(str(num), ":white_check_mark:")

    chance = random.randint(1, 5)
    if chance == 1 or chance == 2 or chance == 3:
      num = random.randint(1, 3)
      array2 = str(array2).replace(str(num), ":white_check_mark:")
      chance = random.randint(1, 6)
      if chance == 1:
        num = random.randint(1, 3)
        array3 = str(array3).replace(str(num), ":white_check_mark:")
        chance = random.randint(1, 7)
        if chance == 1:
          num = random.randint(1, 3)
          array4 = str(array4).replace(str(num), ":white_check_mark:")
          chance = random.randint(1, 8)
          if chance == 1:
            num = random.randint(1, 3)
            array5 = str(array5).replace(str(num), ":white_check_mark:")
            chance = random.randint(1,10)
            if chance == 1:
              num = random.randint(1, 3)
              array6 = str(array6).replace(str(num), ":white_check_mark:")
              chance = random.randint(1, 11)
              if chance == 1:
                num = random.randint(1, 3)
                array7 = str(array7).replace(str(num), ":white_check_mark:")
                chance = random.randint(1, 12)
                if chance == 10:
                  num = random.randint(1, 3)
                  array8 = str(array8).replace(str(num), ":white_check_mark:")

    array1 = str(array1).replace(' [', '').replace('[', '').replace(']', '')
    array2 = str(array2).replace(' [', '').replace('[', '').replace(']', '')
    array3 = str(array3).replace(' [', '').replace('[', '').replace(']', '')
    array4 = str(array4).replace(' [', '').replace('[', '').replace(']', '')
    array5 = str(array5).replace(' [', '').replace('[', '').replace(']', '')
    array6 = str(array6).replace(' [', '').replace('[', '').replace(']', '')
    array7 = str(array7).replace(' [', '').replace('[', '').replace(']', '')
    array8 = str(array8).replace(' [', '').replace('[', '').replace(']', '')

    array1 = str(array1).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:')
    array2 = str(array2).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:')
    array3 = str(array3).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:')
    array4 = str(array4).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:')
    array5 = str(array5).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:')
    array6 = str(array6).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:')
    array7 = str(array7).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:')
    array8 = str(array8).replace(str(1), ':question:').replace(str(2), ':question:').replace(str(3), ':question:')

    
    return f"{array8}\n{array7}\n{array6}\n{array5}\n{array4}\n{array3}\n{array2}\n{array1}"