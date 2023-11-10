''' Функція як об'єкт першого класу '''
'''1) Перша вимога - Функція може бути збережена у змінній чи структурі даних '''

# def mul(a, b):
#     return a * b

# temp_value = mul           # зберігаємо цілу функцію у змінній
# result = temp_value(3, 5)  # викликаю функцію через змінну
# print(temp_value)
# print(result)

###

# field = {
#     'x': 2,
#     'y': 3,
#     'operation': temp_value  # зберігаємо функцію у словник під ключом 'operation'
# }

# res = field.get('operation')(field.get('x'), field.get('y')) # спосіб виклику функції
# print(res)

# res_1 = field.get('operation')(2, 3)                        # спосіб виклику функції
# print(res_1)

'''2) Друга вимога - Функція може бути передана в іншу функцію як аргумент '''

# def mul(a, b):
#     return a * b

# def sub(a, b):
#     return a - b

# def oper(a, b, func):     # func це цункція яку ми передаємо в іншу функцію як аргумент
#     return func(a, b)     # повернення функції з переданими параметрами a, b

# res_mul = oper(2, 3, mul) # як func передаємо функцію mul
# print(res_mul)

# res_sub = oper(2, 3, sub) # як func передаємо функцію sub
# print(res_sub)

# '''3) Третя вимога - функція може бути повернена з функції як результат'''

# def mul(a, b):
#     return a * b

# def sub(a, b):
#     return a - b

# def ops(operator: str):
#     if operator == '*':
#         return mul          # повернення функції mul як результат (mul без дужок ! )
#     elif operator == '-':
#         return sub          # повернення функції sub як результат (sub без дужок ! )
#     else:
#         pass

# func_mul = ops('*')          # змінній func_mul присвоюємо функцію ops('*')
# res_mul = func_mul(2, 5)     # присвоюємо змінній res_mul виклик функції через змінну  

# func_sub = ops('-')          # змінній func_mul присвоюємо функцію ops('-')
# res_sub = func_sub(2, 5)     # присвоюємо змінній res_sub виклик функції через змінну

# print(res_mul)
# print(res_sub)

''' Замикання '''
''' Особливість існування вкладених локальних просторів імен і той факт, що вони створюються динамічно,
дає можливість використати механізм замикань у Python. '''

# def greeting(name):                    # зовнішня функція
#     def message(message):              # внутрішня функція
#         return f'{name}: {message}'    # повернення результату зовнішньої і внутрішньої функцій
#     return message                     # повернення внутрішньої функції (без виклику!!! без дужок () )

# message = greeting('Andrii')           # присвоюємо змінній message функцію greeting з аргументом ('Andrii'), змінна message через замикання має доступ до name-'Andrii' (внутрішні функції мають доступ до зовнішніх фукцій - через замикання)  

# print(message('Hello world!'))

''' Closures (Замикання) '''

# def outer_function(x):                # зовнішня функція
#     y = 10                            # ця змінна буде зберігатись в замиканні

#     def inner_function():             # внутрішня функція має доступ до змінної 'х' з 'outer_function'
#         result = x + y
#         print(f'Result is: {result}')
#     return inner_function             # повертаємо inner_function, яка є замиканням

# closure = outer_function(5)           # створюємо замикання, і передаємо 5 для х

# closure()                             # Викликаємо замикання (замикання можу викликатись в подальших строках)

### 

# def outer(x):
#     def inner(y):
#         print(f'{x} + {y} = {x + y}')
#     return inner

# def main():
#     adder_two = outer(2)        # присвоюємо змінній функцію з аргументом (аргумент 2 запам'ятовується в просторі імен)
#     adder_two(8)                 

# print(main())                   # 2 + 8 = 10

''' застосування кешівання з метою збереження ресурсів'''

# def get_cache(cache = None):
#     if cache is None:
#         cache = {}
#     def inner (n):
#         print(cache)
#         if n not in cache:
#             cache[n] = sum([i for i in range(1, n + 1)])
#             print (f'Hard work: {n}')
#             return cache[n]
#         else:
#             print(f'Easy work: {n}')
#             return cache[n]
#     return inner

# def main():
#     data = {5: 15, 10: 55, 15: 120}
#     calc = get_cache(data)        
#     print(calc(5))
#     print(calc(5))
#     print(calc(10))
#     print(calc(10))
#     print(calc(15))
#     print(calc(5))
   

# print(main())



''' Каррінг - це перетворення функції від багатьох аргументів на набір функцій,
кожна з яких є функцією від одного аргументу. Ми можемо передати частину аргументів у функцію
та отримати назад функцію, чекає на інші аргументи.'''

# def greeting_simple(name, msg):
#     return f'{name}: {msg}'

# print(greeting_simple('Anton', 'Hello world'))
# print(greeting_simple('Natalia', 'Go to home'))

### розбиваємо одну функцію на дві які приймають по одному параметри

# def greeting(name):

#     def simple(msg):
#         return f'{name}: {msg}'

#     return simple

# msg_anton = greeting('Anton')
# print(msg_anton('Hello world'))

# msg_anton = greeting('Natalia')
# print(msg_anton('Go to home'))

'''розбиваємо одну функцію на дві які приймають по одному параметри'''

# def taxer_simple(base_tax, money):
#     if money >= 10000:
#         base_tax = 2.5 * base_tax
#     return money - base_tax * money


# def taxer(base_tax):
#     def calculate(money):
#         nonlocal base_tax
#         if money >= 10_000:
#             base_tax = 2.5 * base_tax  # змінюємо базову ставку
#         return money - base_tax * money

#     return calculate


# money_ukr_vasyl = taxer_simple(0.2, 5000)
# money_ukr_iryna = taxer_simple(0.2, 5500)
# money_ukr_olga = taxer_simple(0.2, 9000)
# money_ukr_petro = taxer_simple(0.2, 9500)
# money_swd = taxer_simple(0.3, 30000)

# print(money_ukr_vasyl)
# print(money_ukr_iryna)
# print(money_ukr_olga)
# print(money_ukr_petro)
# print(money_swd)

###
''' Carring '''
# def greeting (mode):
#     if mode == 'm':
#         return hello_male
#     elif mode == 'f':
#         return hello_famele

# def hello_male(name):
#     print(f'Mr. {name}')

# def hello_famele(name):
#     print(f'Mrs. {name}')

# def main():
#     mr = greeting('m')
#     mrs = greeting('f')

#     mr('Vlad')
#     mrs('Olena')

# print(main())

# if __name__ == '__main':
#     main

''' Carring ''' # (З використанням словника. Дяє можливість розширювати можливості коду без втручання в основну функцію)
# def hello_male(name):
#     print(f'Mr. {name}')

# def hello_famele(name):   # створюємо функцію яка буде повертати f-стрінгу 
#     print(f'Mrs. {name}') 

# def hello_pan(name):      # створюємо функцію яка буде повертати f-стрінгу 
#     print(f'Пан {name}')

# MODES = {                 # створюємо словник значеннями в якому будуть функції  
#     'm': hello_male,      # значення в словнику є функція hello_male з ключем 'm'
#     'f': hello_famele,    # значення в словнику є функція hello_famele з ключем 'а'
#     'pan': hello_pan      # значення в словнику є функція hello_pan з ключем 'pan'
# }

# def greeting (mode):      
#     return MODES[mode]    # функція повертає зі словника функцію яка відповідає переданому ключу 

# def main():                 
#     mr = greeting('m')    # передаємо в функцію greeting аргумент 'm'   (присвоюємо функцію змінній mr)  
#     mrs = greeting('f')   # передаємо в функцію greeting аргумент 'f'   (присвоюємо функцію змінній mrs) 
#     pan = greeting('pan') # передаємо в функцію greeting аргумент 'pan' (присвоюємо функцію змінній pan)

#     mr('Vlad')            # виклик функції чуруз змінну якій присвоєна функція
#     mrs('Olena')          # виклик функції чуруз змінну якій присвоєна функція
#     pan('Taras')          # виклик функції чуруз змінну якій присвоєна функція

# print(main())

# if __name__ == '__main':
#     main

###

# from functools import partial

# def greeting_simple(name, msg):
#     return f'{name}: {msg}'

# msg_anton = partial(greeting_simple, name='Anton')
# print(msg_anton(msg='Go to Lesson'))

''' Декоратори '''
'''Шаблон проектування, який полягає в тому, щоб розширювати існуючий функціонал,
не вносячи змін у код цього самого функціоналу. '''

# def greeting(name):
#     print(f'Hello, my name is: {name}')

# greeting('Alex')                    # функція виконує Hello, my name is: Alex

#                                     # за допомогою декоратора ми не змінюючи першу функцію виводимо новий текст
# def greeting_decorator(func):       # декоратор
#     def wrapper(*args, **kwargs):   # внутрішня функція декоратора зазвичай називається wrapper  або inner
#         print('Test')
#         func(*args, **kwargs)       # викликаємо функцію (greeting)
#         print('Bye, bye!!!')
#     return wrapper

# new_greeting = greeting_decorator(greeting)  # передаєм в функцію greeting_decorator як аргумент функцію greeting
# new_greeting('Olga')

''' Приклад Декоратора без args, kwargs (якщо чітко відомо скільки і яких буде параметрів)'''

# def decorator_name(func):
#     def wrapper(first_name, last_name):
#         print('!' * 5)
#         res = func(first_name, last_name)
#         return res
#     return wrapper


# def prefix_decorator_name(func):
#     def inner(first_name, last_name):
#         print('prefix_decorator_name')
#         return func(first_name, last_name)
#     return inner

# @decorator_name                   # функція задекорована (виклткається декоратором)
# @prefix_decorator_name            # функція задекорована (виклткається декоратором)
# def full_name(first_name, last_name):
#     print(f'Hello {first_name}, {last_name}')

# @decorator_name                   # функція задекорована (виклткається декоратором)
# @prefix_decorator_name            # функція задекорована (виклткається декоратором)
# def test_name(first_name, last_name):
#     print(f'Hello {first_name}, {last_name}')

# full_name('Ivan', 'Melnyk')
# test_name('Olga', 'test')

''' Декоратор для дебагу (отримуємо інформацію про роботу функції, її результат та час роботи ) '''

# from time import time

# def args_logger(func):
#     def inner(*args):
#         if Debug:
#             print(f'I am args logger. Args: {args}')
#         result = func(*args)
#         return result         # повертаємо результат 
#     return inner              # повертаємо саму функцію inner

# def result_logger(func):
#     def inner(*args):
#         result = func(*args)
#         if Debug:
#             print(f'I am result logger. Result: {result}')
#         return result          
#     return inner               

# def timer(func):
#     def inner(*args):
#         start = time()
#         result = func(*args)
#         stop = time()
#         if Debug:
#             print(f'I am timer. Run time: {stop - start}')
#         return result          
#     return inner       


# @timer                # огортаємо функцію calc декоратором timer
# @result_logger       # огортаємо функцію calc декоратором result_logger
# @args_logger         # огортаємо функцію calc декоратором args_logger
# def calc(x, y):      # ця функція буде передаватись в args_logger(func) а аргументи будуть передаватись в inner(*args)
#     result = x + y
#     return result

# Debug = True         # за допомогою цієї змінної можна відключати Декоратор шляхом зміни між True та False

# print(calc(5, 8))

''' Декоратори з параметрами '''

# def repeat_n_times(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator


# @repeat_n_times(5)                  # функція задекорована (виклткається декоратором)
# def greeting(name):
#     print(f'Hello, my name is: {name}')

# greeting('Kristina')


# ''' functools.wrap '''  використовується з метою отримання детальної інформації про задекоровані функції

# import functools

# def my_decorator(func):
#     @functools.wraps(func)               # змінює інформацію яку ми отримуємо про функцію
#     def wrapper(*args, **kwargs):
#         print('Before func is called!')
#         res = func(*args, **kwargs)
#         print('After func is called!')
#         return res

#     return wrapper

# @my_decorator
# def greeting(name):
#     """
#     This function is very important
#     :arg: name: Str....
#     :return: None
#     """
#     print(f'Hello: {name}')


# greeting('Anton')


# # print(greeting.__name__)
# # print(greeting.__doc__)
# # print(help(greeting))

# # wrapper
# # None
# # Help on function wrapper in module __main__:
# #
# # wrapper(*args, **kwargs)
# #
# # None

''' map - функція яка виконує одну і ту саму дію для всіх елементів іиеруємого об’єкта та повертає новий ітеруємий об’єкт.
Функція map приймає щонайменше 2 аргументи. Перший - функція, що буде викликатися для всіх елементів ітеруємого об’єкта, а другий - сам ітеруємий об’єкт.'''

# Вам задано рядок символів s. Виведіть суму ASCII значень всіх символів
# s = input()
# x = 0
# for item in s:
#     x += ord(item)
# print(x)

### те саме в одну строку за допомогою функції map

# print(sum(map(ord, input())))

''' map + lamda # Потрібно щоб кожне ім'я було з великої літери '''

# names = ["dan", "jane", "steve", "mike"]   

# # 1
# def normalize(name):
#     return name.title()

# new_name = []
# for name in names:
#     new_name.append(name.title())
# print(new_name)

# new_name_map = map(normalize, names)
# print(new_name_map)
# print(list(new_name_map))

# # 2
# new_name_map = map(str.title, names)
# print(list(new_name_map))

# # 3
# # new_name_map = map(lambda name: name.title(), names)
# new_name_map = list(map(lambda name: name.title(), names))
# print(new_name_map)

# # 4
# new_name_map = [name.title() for name in names]
# print(new_name_map)

''' map + lambd - перебирання двох колекцій (кількості об'єктів ітерації має дорівнювати кількості аргументів)'''

# list_1 = [1, 2, 3, 4, 5]  # якщо кількості елементів колекції не співпадають то обраобка зупиниться після закінчення елементів меншої колекції
# list_2 = ['a', 'b', 'c', 'd', 'e']

# for n in map(lambda x, y: f'{y}: {x}', list_1, list_2):
#     print(n)

''' filter - аналогічна до map функція тільки filter повертає тільки елементи які дають True ''' 
# простіший приклад фільтра

# print(list(filter(lambda i: i % 2, range(10)))) # виведення непарних чисел від 1 до 9

###

# payment = [100, -3, 400, 35, -100]

# def is_negative_number(num) -> bool:
#     if num < 0:
#         return True
#     return False

# result = filter(is_negative_number, payment)
# print(list(result))


# def is_positive_number(num):
#     if num > 0:
#         return True
#     return False

# result = filter(is_positive_number, payment)
# print(list(result))

# result = list(filter(lambda num: num > 0, payment))
# print(result)

# result = list(filter(lambda num: num < 0, payment))
# print(result)

''' filter. перевірка послідовності на остачу від ділення '''

# data = [1, 2, 3, 4, 5, 6]

# def check_num(data):
#     result = []
#     for n in data:
#         ost = n % 2
#         if ost:
#             result.append(n)
#     return result   

# chech_data = check_num(data)
# print(*chech_data)

### тес аме через функцію filter

# chech_data_filter = filter(lambda x: x % 2, data)
# print(*chech_data_filter)

### або
# print(*filter(lambda x: x % 2, data))

''' map and filter - поєднання двох функцій '''

# # 1
# nums = [i for i in range(1, 10)]
# print(nums)
# sq = map(lambda x: x ** 2, nums)

# result = filter(lambda value: not bool(value % 2), sq)
# print(list(result))

# # 2
# result = filter(lambda value: not bool(value % 2), map(lambda x: x ** 2, [i for i in range(1, 10)]))
# print(list(result))

# # 3
# result = list(map(lambda x: x ** 2, filter(lambda value: not bool(value % 2), [i for i in range(1, 10)])))
# print(result)

''' yield - найпростіший генератор (на відміну від return при наступному зверненні не розпочинає виконання з початку а запам'ятовує місце зпинки виконання)'''

# def simple_generator():
#     yield 'Test'
#     yield 'Hello'
#     yield 'world'

# for item in simple_generator():
#     print(item)                     # Test Hello world

''' генератор за допомогою yield та next'''
# def my_range(limit):
#     value = 0
#     while value < limit:
#         yield value
#         value += 1

# gen = my_range(5)
# # for number in my_range(5):
# #     print(number)

# while True:
#     try:
#         r = next(gen)
#         print(r)
#     except StopIteration:
#         break

''' next (самовстійний виклик через next) '''

# def simple_generator():
#     yield 'Test'
#     yield 'Hello'
#     yield 'world'

# gen = simple_generator()
# print(gen)

# r_next = next(gen)      
# print(r_next)  
# r_next = next(gen)
# print(r_next)               # при кожному виклику функції виводить одне значення
# r_next = next(gen)
# print(r_next)               # при виклику більше ніж є yield буде викликане виключення StopIteration 

''' Лямбда функція (анонімна функція - яка не присвоюється змінній) lambda x, y, z: x * y * z. Використовується для вирішення простих задач '''
# def pow_normal(x):
#     return x ** 2

# pow_lambda = lambda x: x ** 2

# print(pow_normal(5))
# print(pow_lambda(5))

###
# import math

# def get_length(d):                        # множення на число пі за допомогою звичайної функції
#     result = d * math.pi
#     return result

# get_lambda_length = lambda d: d * math.pi # множення на число пі за допомогою лямбда функції (замість 3-х строк зробили в одну)
    
# lenght_1 = get_length(10)
# lenght_2 = get_lambda_length(10)
# print(lenght_1, lenght_2, sep = '\n' )

### отримання остачі від числа

# def get_ost(data):
#     result = []
#     for n in data:
#         ost = n % 2
#         result.append(ost)
#     return result

# data = [1, 2, 3, 4, 5, 6]
# ost_1 = get_ost(data)
# print(*ost_1)                       # за допомогою оператора * розпаковується список

# print(*map(lambda n: n % 2, data))  # те саме за допомогою ламбда функції в одну строку

''' reduce - приміняє функцію function до усіх елементів послідовності iterable, зводячи її до єдиного значення '''   
''' reduce(function, iterable[, initializer]) - func : Функция, яку потрібно застосувати до елементів послідовності. Повинна приймати два аргументи, де перший аргумент — аккумулює попереднє значення, а другий — наступний элемент послідовності.
iterable : Последовність, элементи якої потрібно звести до єдиного значення. Якщо послідовність пуста і не задано initializer, то виникає TypeError.
initializer=None: Базове значення, з якого потрібно почати відлік. Воно ж буде повернуто, якщо послідовність пуста (не обов'язково).'''

# from functools import reduce

# def add(x, y):
#     return x * y


# numbers = [2, 3, 4, 5]

# result = reduce(add, numbers)  # (((2*3)*4)*5) = 120
# # result = reduce(add, numbers, 5) # (((5*2)*3)*4)*5)) = 600
# print(result)
