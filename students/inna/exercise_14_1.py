import time
from datetime import date
today = date.today()

groceries = [('cheese', 7.99), 
             ('eggs', 3.99), 
             ('bread', 6.99), 
             ('milk', 2.99)]

# initialize it outside of the loop
running_total = 0

for item in groceries:
    name = item[0]
    price = item[1]
    print(name)
    running_total += price # equivalent to "running_total = running_total + price"

running_total = '{:.2f}'.format(running_total)

print(f'purchase total today on {today} is ${running_total}')