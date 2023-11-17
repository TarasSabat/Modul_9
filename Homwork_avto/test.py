
def get_emails(list_contacts):
    # Використовуємо map для отримання електронних адрес з кожного словника контакту
    emails = list(map(lambda contact: contact["email"], list_contacts))
    return emails

# Приклад використання:
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    # Додайте інші контакти, якщо потрібно
]

result_emails = get_emails(contacts)
print(result_emails)


    