import os

def clear() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def ask_int(str: str) -> int:
    while True:
        try:
            choice = int(input(str))
            return choice
        except ValueError:
            continue