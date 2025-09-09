import matplotlib.pypot as plt
import numpy as np

#Creating a sample data
months = ['Jan', 'Feb', 'March', 'April']
sales = [536, 8939, 1000, 67378]

x = np.array([300, 100, 12, 562, 266])
#Simple data for three products
#Sales data for three products over 6 months
product_A_sales = np.array([100, 120, 45, 111,90])

plt.plot(x, product_A_sales, marker=0, label="")

