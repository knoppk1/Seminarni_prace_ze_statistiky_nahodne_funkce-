from random_lib import getrandomint
from secrets_lib import getsecretint

ITERATIONS = 10000
AMOUNT_OF_NUMBERS = 10

def weighted_avarage(num_dict):
    numbers = num_dict
    w_avarage = 0
    sum = 0

    for num in numbers:
        frequency = numbers[num]
        sum += frequency
        w_avarage += num*frequency
    
    w_avarage = w_avarage/sum

    return w_avarage

secret = getsecretint(ITERATIONS, AMOUNT_OF_NUMBERS)
random = getrandomint(ITERATIONS, AMOUNT_OF_NUMBERS)

w_a_secret = weighted_avarage(secret)
w_a_random = weighted_avarage(random)

print(f"random lib: {random} weighted avg: {w_a_random}")
print(f"secret lib: {secret} weighted avg: {w_a_secret}")