contacts = {}
exit_commands = ("good bye", "close", "exit")


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'Given name is not in the list'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Please enter the correct name and phone number'
    return inner


@error_handler
def parse_command(user_input):
    commands = user_input.lower().split()
    if commands[0] == 'hello':
        return handle_hello()
    elif commands[0] == 'add':
        return handle_add(commands[1], commands[2])   
    elif commands[0] == 'change': 
        return handle_change(commands[1], commands[2])
    elif commands[0] == 'phone': 
        return handle_phone(commands[1]) 
    elif commands[0] == 'show' and  commands[1] == 'all':
        return handle_show_all()
    

def handle_hello():
    return "How can I help you?"

def handle_add(name, phone):
    contacts.update({name.capitalize(): phone})
    print(name.capitalize(), phone)
    return "Contact added"

def handle_change(name, phone):
    if name.capitalize() in contacts:
        contacts[name.capitalize()] = phone
        print(contacts)
        return "Contact's phone number has changed"
    else:
        return "Given name is not in the list"

def handle_phone(name):
    name = name.capitalize()
    phone = contacts[name]
    print(phone)
    return "Phone number for the specified contact is displayed"

def handle_show_all():
    print(contacts)
    return "All saved contacts are displayed"
        
 
while True:    
    user_input = input("... ")
    command = user_input.lower()
    try:
        if command.split()[0] in exit_commands:
            print("Goodbye !")
            break
    except IndexError:
        print("Enter the correct command")
        continue
    result = parse_command(command)
    print(result)



    

      









