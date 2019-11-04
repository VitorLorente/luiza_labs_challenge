import sys

def make_migrate(customers=0):
    from setup.migrate import migrate
    migrate(customers)

def make_runserver(port=8080):
    from server.server import runserver
    runserver(port)

def return_message_error():
    return_string = "\nCOMMAND ERROR\n\nOptions are:\n\n\t- migrate [initial_users];\n\t- serverup [port_number];\n\n"
    print(return_string)

commands = {
    'migrate': make_migrate,
    'serverup': make_runserver,
}

if len(sys.argv) == 3:
    command = commands.get(sys.argv[1], None)
    if command:
        command(int(sys.argv[2]))
    else:
        return_message_error()
elif len(sys.argv) == 2:
    command = commands.get(sys.argv[1], None)
    if command:
        command()
    else:
        return_message_error()
else:
    return_message_error()
