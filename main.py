from fizz import Fizz
from buzz import Buzz
from fizzbuzz import Fizzbuzz

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        Fizzbuzz.fizzbuzz(i)
    if i % 3 == 0 and i % 5 != 0:
        Fizz.fizz(i)
    if i % 5 == 0 and i % 3 != 0:
        Buzz.buzz(i)
    elif (i % 3 != 0 and i % 5 != 0):
        print(i)
