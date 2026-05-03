def parse_input(user_input):
  
    parts = user_input.split()
    if not parts:
        return "", []
    
    cmd = parts[0].strip().lower()
    args = parts[1:]
    
    return cmd, args


def add_contact(args, contacts):

    if len(args) < 2:
        return "Помилка: введіть ім'я та номер телефону."
    
    name = args[0]
    phone = args[1]
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
  
    if len(args) < 2:
        return "Помилка: введіть ім'я та новий номер телефону."
    
    name = args[0]
    phone = args[1]
    
    if name not in contacts:
        return f"Помилка: контакт '{name}' не знайдено."
    
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):

    if len(args) < 1:
        return "Помилка: введіть ім'я контакту."
    
    name = args[0]
    
    if name not in contacts:
        return f"Помилка: контакт '{name}' не знайдено."
    
    return contacts[name]


def show_all(contacts):

    if not contacts:
        return "Записник порожній."
    
    result = "Ваші контакти:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    
    return result.strip()


def main():
    """
    Основна функція бота-помічника.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(args, contacts))
        
        elif command == "change":
            print(change_contact(args, contacts))
        
        elif command == "phone":
            print(show_phone(args, contacts))
        
        elif command == "all":
            print(show_all(contacts))
        
        elif command == "":
            continue
        
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()