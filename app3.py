try:
    first_name = str(input(">Name: "))
    last_name = str(input(">Last Name: "))
    age = int(input(">age: "))
except ValueError:
    print('Invalid value')
if ValueError:
    age = int(input(">age: "))


def default_user(first_name):
    print(f'{first_name} ')
    print('Welcome aboard')


def ex_default_user(first_name, last_name, age):
    print(f'{first_name} {last_name}, {age}')


print("""
    help: for commands
    info: for simple information
    exinfo: for extended information
    stop: to end session
    """)
command = ""

while (command.lower()) != "stop":

    command = int(input("> "))
    if command == "help":
        print("""
help: for commands
info: for simple information
exinfo: for extended information
stop: to end session
""")
    elif command == "info":
        default_user(first_name)
    elif command == "exinfo":
        ex_default_user(first_name, last_name, age)
    elif command == "stop":
        print("See you later! ")
        break
    else:
        print("Sorry, I dont understand that..")
