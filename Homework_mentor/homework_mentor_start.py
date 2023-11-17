# початковий варіант (доопрацьовувався)
contacts = {'Taras': '0961624814', 'Irina': '0677107670'}



while True:
    hello_1 = input(':')
    hello_1 = hello_1.lower()
    if hello_1 == 'hello':
        hello_1 = input("How can I help you?" '\n:').lower()
    if hello_1.startswith('add'):
        add = hello_1.split()
        contacts.update({add[1].capitalize(): add[2]})
        continue
    elif hello_1.startswith('change'):
        change = hello_1.split()
        contacts[change[1].capitalize()] = change[2]
        continue
    elif hello_1.startswith('phone'):
        phone = hello_1.split()
        name = phone[1].capitalize()
        print(contacts.get(name))
        continue
    elif hello_1.startswith('show all'):
        print(contacts)
        continue
    elif hello_1 == 'good bye' or hello_1 == 'close' or hello_1 == 'exit':
        print('Good bye!')
        break