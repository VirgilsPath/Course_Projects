from functools import reduce

costs = {"shirt": (4, 13.00), "shoes":(2, 80.00), "pants":(3, 100.00), "socks":(5, 5.00), "ties":(3, 14.00), "watch":(1, 145.00)}

nums = (24, 6, 7, 16, 8, 2, 3, 11, 21, 20, 22, 23, 19, 12, 1, 4, 17, 9, 25, 15)

# Code for Checkpoint 1 goes here.

total = reduce(lambda x, y: x + y, filter(lambda x: x > 150, map(lambda x: costs[x][0] * costs[x][1], costs)))

print(total)

product = -1

# Code for Checkpoint 2 goes here.

product = reduce(lambda x, y: x * y, map(lambda x: x + 5, filter(lambda x: x < 10, nums)))

print(product)