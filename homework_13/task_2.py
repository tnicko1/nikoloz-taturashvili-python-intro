"""
Create three lists and fill them with random numbers.
Print the sums of numbers at the same index on the screen.
"""

from random import randint

list1 = [randint(1, 100) for _ in range(10)]
list2 = [randint(1, 100) for _ in range(10)]
list3 = [randint(1, 100) for _ in range(10)]


for i in range(len(list1)):
    _sum = list1[i] + list2[i] + list3[i]
    print(f"{i}  |  {list1[i]}  +  {list2[i]}  +  {list3[i]}  =  {_sum}")

