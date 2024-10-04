from util import ask_int, clear, is_binary, menu

flag1 = True

while flag1:
    clear()
    print("\tMain Menu\n")
    print("1. L1 (Starts with '10' & ends with '01')")
    print("2. L2 (Contains '000' & ends with '1')")
    print("3. L3 (Starts & ends with different symbol)")
    print("4. L4 (Starts & ends with same symbol & contains '101')")
    print("5. Exit\n")
    choice = ask_int("\tChoice: ")
    if choice == 5:
        flag1 = False
    else:
        menu(choice)