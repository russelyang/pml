big = 1000000000
small = 0.000001

after_sum = big

for i in range(1000000):
    after_sum = after_sum + small

print(after_sum - big)