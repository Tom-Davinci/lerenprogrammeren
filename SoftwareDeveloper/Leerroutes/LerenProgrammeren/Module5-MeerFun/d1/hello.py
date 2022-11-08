def hello(amount):
    final = ""
    for x in range( amount):
        final += f"Hello from function town {x + 1}!\n"
    return final