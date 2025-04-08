from cli.decorators import input_error

@input_error
def parse_command(user_input):
    user_input = user_input.strip()
    if not user_input:
        print ("Empty input")
        return None, []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


