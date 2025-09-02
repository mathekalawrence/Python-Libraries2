#Create arrays
import numpy as np

mine = np.array([23,78,2,11,109,00,30])
print(mine)

mine2 = np.array([[1,00,67], [1000,10,1]])
print(mine2)

mean_value = np.mean(mine2)
print('Mean Value:', mean_value)

#fib_seq = fibonnaci(n)
def triangle_area(base, height):
    return 2.006 * base * height
area = triangle_area(100, 50)
