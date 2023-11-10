''' Closures (Замикання) '''

# def taxer(base_tax):
#     def calculate(money):
#         nonlocal base_tax
#         if money >= 10000:
#             base_tax = 2 * base_tax  # змінюємо базову ставку
#         return money - base_tax * money
#     return calculate

# ukr = taxer(0.1)  # %
# nrw = taxer(0.45)  # %

# money_ukr = ukr(9500)
# money_nrw = nrw(25000)
# print(money_ukr)
# print(money_nrw)

''' Зробити декоратор, який повертає кортеж з результатом функції обчислення факторіал та часом її виконання '''

# from time import time, sleep

# def time_counter_decorator(func):        # декоратор
#     def interval(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         passed = time() - start
#         return result, passed
#     return interval

# @time_counter_decorator
# def caching_fibonacci(n):
#     cache = {}
#     sleep(2)

#     def fibonacci(n):

#         if n in cache:
#             return cache[n]
#         elif n <= 1:
#             return n
#         else:
#             fibonachi_cache = fibonacci(n - 1) + fibonacci(n - 2)
#             cache[n] = fibonachi_cache
#             return fibonachi_cache

#     return fibonacci(n)


# f8 = caching_fibonacci(19)
# print(f'f8: {f8}')

# @time_counter_decorator
# def test_func(x, y):
#     sleep(3)
#     return x * y

# print(test_func(3, 5))


###

# def outer(x):
#     def inner(y):
#         print(f'{x} + {y} = {x + y}')
#     return inner

''' Напишіть decorator, який записує в консоль два повідомлення журналу:
: call [номер_виклику_функції]: [ім'я функції][її аргументи]\n
: result: [ім'я функції][результат]\n
'''

# import sys

# def logger(func):
#     counter = 0
#     def inner(*args, **kwargs):
#         nonlocal counter
#         counter += 1
#         sys.stdout.write(f": call [{counter}]: [{func.__name__}][{args}]\n")
#         result = func(*args, **kwargs)
#         sys.stdout.write(f": result: [{func.__name__}][{result}]\n")
#         return result
#     return inner

# @logger
# def add(x, y):
#     return x + y


# @logger
# def sub(x, y):
#     return x - y


# print(add(4, 5))
# print(add(33, 11))
# print(sub(33, 11))
# print(add(1, 4))
# print(sub(5, 6))

''' Генератор повернення, який повертає ціле число між min_val та max_val у нескінченному циклі '''
 
# from random import randint, seed


# def cycle_random(min_val, max_val):
#     seed()
#     while True:
#         yield randint(min_val, max_val)


# rand_gen = cycle_random(5, 15)
# result = []
# for _ in range(100):
#     result.append(next(rand_gen))

# print(result)

