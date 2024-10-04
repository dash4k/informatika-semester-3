import os
from dfa import l1, l2, l3, l4

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

def is_binary(str: str):
    return set(str).issubset({'0', '1'})

def menu(l: int):
    if l > 4 or l < 1:
        return
    flag2 = True
    while flag2:
        clear()
        print("Insert a binary value (0, 1) to continue, else insert 'cancel'\n")
        x = input("Input: ")
        if x.lower() == 'cancel':
            flag2 = False
            continue
        elif not is_binary(x):
            input("Alert! The current input contains values outside of the binary range (i.e., 0 and 1)\n\nPress enter to continue...............")
            continue
        else:
            if l == 1:
                print("\nThe current input starts with '10' & ends with '01'") if l1(x) else print("\nThe current input does not starts with '10' & ends with '01'")
                input("\nPress enter to continue...............")
                continue
            elif l == 2:
                print("\nThe current input contains '000' & ends with '01'") if l2(x) else print("\nThe current input does not contains '000' & ends with '01'")
                input("\nPress enter to continue...............")
                continue
            elif l == 3:
                print("\nThe current input starts & ends with different symbol") if l3(x) else print("\nThe current input does not starts & ends with different symbol")
                input("\nPress enter to continue...............")
                continue
            elif l == 4:
                print("\nThe current input starts & ends with same symbol & contains '101'") if l4(x) else print("\nThe current input does not starts & ends with same symbol & contains '101'")
                input("\nPress enter to continue...............")
                continue