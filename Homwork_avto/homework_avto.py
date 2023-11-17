'''№ 1
Повернемося до завдання про систему оцінок в університеті, які мають такий вигляд:
Оцінка	Бали	Оцінка ECTS	Пояснення
1	0-34	F	Unsatisfactorily
2	35-59	FX	Unsatisfactorily
3	60-66	E	Enough
3	67-74	D	Satisfactorily
4	75-89	C	Good
5	90-95	В	Very good
5	96-100	A	Perfectly
Минулого разу ми реалізували дві функції. Перша - get_grade, приймає ключ в оцінці ECTS і повертає відповідну п'ятибальну оцінку (перший стовпчик таблиці). Друга - get_description, теж приймає ключ у оцінки ECTS, але повертає пояснення оцінки у текстовому форматі (останній стовпчик таблиці). На неіснуючий ключ функції повинні повертати значення None.
Реалізуйте функцію вищого порядку get_student_grade, яка приймає параметр option. Якщо він дорівнює значенням "grade", то функція повертає функцію get_grade, а якщо його значення дорівнює "description", то повертає функцію get_description. Якщо параметр за значенням не співпав із заданими, то функція get_student_grade повинна повертати значення None.
'''

# def get_grade(key):
#     grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
#     return grade.get(key, None)


# def get_description(key):
#     description = {
#         "A": "Perfectly",
#         "B": "Very good",
#         "C": "Good",
#         "D": "Satisfactorily",
#         "E": "Enough",
#         "FX": "Unsatisfactorily",
#         "F": "Unsatisfactorily",
#     }
#     return description.get(key, None)

# def get_student_grade(option):
#     if option == "grade":
#         return get_grade
#     elif option == "description":
#         return get_description
#     else:
#         return None

'''№2
Реалізуйте функцію get_discount_price_customer для розрахунку ціни на товар інтернет-магазину з урахуванням знижки клієнта.
Функція приймає два параметри:
price — ціна продукту
customer — словник з даними клієнта такого виду: {"name": "Dima"} або {"name": "Boris", "discount": 0.15}
Ви маєте глобальну змінну DEFAULT_DISCOUNT, яка визначає знижку для клієнта, якщо у нього немає поля discount.
Функція get_discount_price_customer має повертати нову ціну товару для клієнта.
Нагадаємо, що дисконт discount - це дробове число від 0 до 1. І ми під знижкою розуміємо коефіцієнт, який визначає величину ціни. І на цю величину ми знижуємо підсумкову ціну товару: price = price * (1 - discount).
'''
# DEFAULT_DISCOUNT = 0.05


# def get_discount_price_customer(price, customer):
#     if len(customer) == 1:
#         price = price * (1 - DEFAULT_DISCOUNT)
#         return price 
#     else:
#         price = price * (1 - customer.get("discount"))
#         return price

# print(get_discount_price_customer(10, {"name": "Dima"}))
# print(get_discount_price_customer(10, {"name": "Boris", "discount": 0.15}))

'''№3
Концепцію замикання може добре пояснити приклад кешування значень функції.
Підсумкове завдання модуля 3 було — рекурсивне обчислення чисел Фібоначчі.
Ряд Фібоначчі - це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ..., де кожне наступне число послідовності виходить додаванням двох попередніх членів ряду.
У загальному вигляді для обчислення n-го члена ряду Фібоначчі потрібно вирахувати вираз: Fn = Fn-1 + Fn-2.
Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює числа послідовності доти, доки виклик не сягне членів ряду менше n = 1, де послідовність задана.
Створіть функцію caching_fibonacci(), яка матиме кеш із попередньо обчисленими значеннями чисел Фібоначі. Усередині вона містить функцію fibonacci(n), яка безпосередньо і обчислюватиме саме число Фібоначчі. Функція caching_fibonacci() повертає функцію fibonacci
Якщо число Фібоначчі зберігається у словнику cache, то функція fibonacci повертає число з кеша. Якщо його немає у кеші, то ми обчислюємо число і поміщаємо його в кеш, і повертаємо з функції fibonacci.
'''

# def caching_fibonacci(cache = None):
#     if cache is None:
#         cache = {}
#     def fibonacci(n):
#         if n not in cache:
#             if n in (1, 2):
#                 return 1
#             elif n == 0:
#                 return 0
#             else:
#                 cache[n] = fibonacci(n-1)+fibonacci(n-2)
#                 return cache[n]
#         else:
#             return cache[n]
#     return fibonacci

# fib = caching_fibonacci(cache = None)
# print(fib(3))
# print(fib(5))
# print(fib(3))

'''№4
Повернемося до завдання розрахунку ціни з урахуванням дисконту та розберемо підхід із позиції карування. Створіть функцію discount_price(discount), яка визначатиме в собі та повертатиме функцію розрахунку реальної ціни з урахуванням знижки.
Виклик функції discount_price(discount) поверне функцію, яка розраховує ціну на товар зі знижкою, що дорівнює discount .
Наприклад:
cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))
Повинен вивести:
85.0
90.0
95.0
'''
# def discount_price(discount):
#     def disc(price):
#         return price * (1 - discount)
#     return disc
    

# cost_15 = discount_price(0.15)
# price = 100
# print(cost_15(price))

'''№5
У модулі 5 ми написали функцію sanitize_phone_number для нормалізації рядка з телефонним номером. Нагадаємо, що при отриманні рядків

    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
Ми отримували наступний вивід:

380501233234
0503451234
0508889900
380501112222
380501112211
Уявіть, що в іншому місці програми у нас виникла вимога зробити висновок у форматі

+380501233234
+380503451234
+380508889900
+380501112222
+380501112211
І тут ідеально підійде створення декоратора для функції sanitize_phone_number. Декоратор повинен додавати для коротких номерів префікс +38, а для повного міжнародного номера (з 12 символом) - тільки знак +. Реалізуйте декоратор format_phone_number для функції sanitize_phone_number з необхідним функціоналом.
'''
# def format_phone_number(func):
#     def inner(phone):
#         new_phone = func(phone)
#         if len(new_phone) == 10:
#             result = '+38' + new_phone
#             return result
#         else:
#             result = '+' + new_phone
#             return result
#     return inner


# @format_phone_number
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#             .removeprefix("+")
#             .replace("(", "")
#             .replace(")", "")
#             .replace("-", "")
#             .replace(" ", "")
#     )
#     return new_phone

# print(sanitize_phone_number('+38(050)123-32-34'))

'''№6
Нехай є рядок з числами (з метою спрощення числа лише цілі), що визначає якісь частини загального доходу. Наприклад,
"The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
Необхідно реалізувати функцію generator_numbers, яка буде парсити рядок і знаходити всі цілі числа в ньому та працювати як генератор, який буде віддавати зазначені числа при зверненні до нього у циклі.
З парсингом рядків ми вже зіштовхувалися виконуючи завдання модуля 7, коли розбивали на лексеми арифметичний вираз
Функція generator_numbers(string="") безпосередньо розпарсює рядок і за допомогою yield повертає поточне число.
Функція sum_profit(string) підсумовує числа, отримані від generator_numbers, та повертає загальну суму прибутку з рядка.
'''
# import re

# def generator_numbers(string=""):
#     for numeric in re.findall(r'\d+', string):
#         yield numeric
    

# def sum_profit(string):
#     numeric_get = generator_numbers(string)
#     sum = 0
#     for n in numeric_get:
#         sum += int(n)
#     return sum

# sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000.")      
    
'''№7
Є список name з іменами користувачів, але всі починаються з малої літери.
name = ["dan", "jane", "steve", "mike"]
Розробіть функцію normal_name, яка приймає список імен та повертає теж список імен, але вже з правильними іменами з великої літери.
['Dan', 'Jane', 'Steve', 'Mike']
Необхідно використовувати функцію map. Не забудьте, що необхідно виконати перетворення типів для map.
'''
# # Варіант 1

# name = ["dan", "jane", "steve", "mike"]

# def normal_name(list_name):
#     new_name_map = map(str.capitalize, list_name) 
#     return list(new_name_map)
    
# print(normal_name(name))

# # Варіант 2

# name = ["dan", "jane", "steve", "mike"]

# def normal_name(list_name):
#     new_name_map = map(str.title, list_name)  
#     return list(new_name_map)
    
# print(normal_name(name))

'''№8
Є список contacts, елементи якого - словники контактів наступного виду:
{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.
Розробіть функцію get_emails, яка отримує у параметрі список list_contacts та повертає список, який містить електронні адреси всіх контактів зі списку list_contacts. Використовуйте функцію map.
'''

# def get_emails(list_contacts):
#     emails = list(map(lambda contact: contact["email"], list_contacts))
#     return emails

# contact = [
#     {'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, 
#     {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': False}, 
#     {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, 
#     {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': False}]

# result_emails = get_emails(contact)
# print(result_emails)

'''№9
На початку четвертого модуля ми вирішували завдання виплат за комунальними платежами. Вони являли собою список payment з додатними та від'ємними значеннями. Створіть функцію positive_values та за допомогою функції filter відфільтруйте список payment за додатними значеннями, та поверніть його з функції.
payment = [100, -3, 400, 35, -100]
'''
# payment = [100, -3, 400, 35, -100]

# def positive_values(list_payment):
#     result = list(filter(lambda n: n > 0, list_payment))
#     return result
  
# print(positive_values(payment))

'''№10
Є список contacts, елементи якого - словники контактів наступного виду:
    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.
Створіть функцію get_favorites(contacts), яка повертатиме список, який містить лише обрані контакти. Використовуйте при цьому функцію filter, щоб відфільтрувати по полю favorite лише обрані контакти.
'''
# contacts = [{
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False},
#     {"name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": True,
# }]

# def get_favorites(contacts):
#     contacts_list = list(filter(lambda contact: contact.get("favorite", False), contacts)) 
#     return contacts_list

# print(get_favorites(contacts))

'''№11
Для списку numbers підрахувати суму елементів за допомогою функції reduce.
numbers = [3, 4, 6, 9, 34, 12]
Створіть функцію sum_numbers(numbers), результатом виконання якої буде сума чисел всіх елементів списку numbers.
'''

# from functools import reduce


# def sum_numbers(numbers):
#     result = reduce(lambda x, y: x + y, numbers)
#     return result

'''№12
Повернемося до нашого першого завдання з четвертого модуля і перепишемо його за допомогою функції reduce.
payment = [1, -3, 4]

def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum
Нагадаємо умову. У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, якщо необхідно сплатити за рахунками. За допомогою reduce підсумуйте додатні значення та поверніть з функції amount_payment суму платежу в кінці місяця.
'''
# from functools import reduce


# def amount_payment(payment):
#     result_1 = list(filter(lambda x: x > 0, payment))
#     result_2 = reduce(lambda x, y: x + y, result_1)
#     return result_2

# print(amount_payment([100, -3, 400, 35, -100]))
    

                    
                    