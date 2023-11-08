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

### розбиваємо одну функцію на дві які приймають по одному параметри

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

# ''' Декоратори з параметрами '''

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
