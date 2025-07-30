def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Username's phone changed."
    else:
        return f"Username {name} is not in contacts."
    
    
def phone_username(args, contacts):
    username = args[0]
    if username in contacts.keys():
        return contacts[username]
    else:
        return f"Username {username} is not in contacts."
    

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
            print(phone_username(args, contacts))
        elif command == "all":
            for key, value in contacts.items():
                print(key, value)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
