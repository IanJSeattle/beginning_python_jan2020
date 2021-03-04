"""
this script generates some interesting data in CSV format
"""

import random

# print(random.randint(0, 10))  #print out a single random number

fp = open('data.csv', 'w')

for i in range(100):
    my_rand = random.randint(0, 100)
    fp.write(str(my_rand) + '\n')

fp.close()
