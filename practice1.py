import math
import random
import datetime

print(math.sqrt(56))
print(math.pi)

#print(math.acos(345))
print("Power of 4^6:", math.pow(4, 6))
print("Random number between 2 and 27:", random.randint(2, 27))

today = datetime.date.today()
print("The date is: ", today)

now = datetime.datetime.now()
print("The current time is:", now.strftime("%H:%M:%S"))
