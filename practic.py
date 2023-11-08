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