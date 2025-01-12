import math, sys

def GetDivisors(n):
    small_divisors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors

target = int(sys.stdin.read())
count = 0
while True:
    count += 1
    divisors = GetDivisors(count)
    if sum(divisors) * 10 >= target:
        break
print(count)