commands = []


def register_command(command):
    global commands
    commands.append(command)
    return command
