import os
import curses
from dfa import l1, l2, l3, l4
from delta_dfa import l1_delta, l2_delta, l3_delta, l4_delta

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
                print("\nThe current input starts & ends with identical symbol & contains '101'") if l4(x) else print("\nThe current input does not starts & ends with identical symbol & contains '101'")
                input("\nPress enter to continue...............")
                continue

def print_menu(stdscr, selected: int, menu: list):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for i, title in enumerate(menu):
        x = w//2 - len(title)//2
        y = h//2 - len(menu)//2 + i
        if i == selected:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, title)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, title)

def l1_iterative(stdscr):
    h, w = stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()
    pad = curses.newpad(100, w)
    flag2 = True
    buffer = ""
    state = " A"
    stdscr.addstr(0, 0, "Insert a binary value (0, 1) to continue, press 'ESC' to go back, press 'Enter' to reset")
    stdscr.refresh()
    while flag2:
        x = stdscr.getch()
        if x in [48, 49]: # 48 == '0' and 49 == '1'
            if len(state) > w-6:
                pass
            else:
                buffer += chr(x)
                state += " --> " + l1_delta(state[-1], buffer[-1])
        elif x == curses.KEY_BACKSPACE or x == 127: # 127 == Backspace
            if buffer == "":
                continue
            buffer = buffer[:-1]
            state = state[:-6]
        elif x == 27: # 27 = Esc
            break
        elif x == curses.KEY_ENTER or x in [10, 13]: # 10 == '\n', 13 == '\r'
            buffer = ""
            state = " A"
            pass
        pad.clear()
        pad.addstr(0, 0, f"Input: ")
        pad.attron(curses.color_pair(1))
        pad.addstr(0, 7, buffer)
        pad.attroff(curses.color_pair(1))
        pad.addstr(1, 0, state)
        if state[-1] == 'F':
            pad.addstr(4, 0, "The current input starts with '10' & ends with '01'")
        else:
            pad.addstr(4, 0, "The current input does not starts with '10' & ends with '01'")
        if len(state) > w-6:
            pad.addnstr(3, 0, "Slow down there buckaroo, too many of states already been processed!", w, curses.A_UNDERLINE | curses.A_REVERSE)
        pad.refresh(0, 0, 2, 0, 11, w)

def l2_iterative(stdscr):
    h, w = stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()
    pad = curses.newpad(100, w)
    flag2 = True
    buffer = ""
    state = " A"
    stdscr.addstr(0, 0, "Insert a binary value (0, 1) to continue, press 'ESC' to go back, press 'Enter' to reset")
    stdscr.refresh()
    while flag2:
        x = stdscr.getch()
        if x in [48, 49]: # 48 == '0' and 49 == '1'
            if len(state) > w-6:
                pass
            else:
                buffer += chr(x)
                state += " --> " + l2_delta(state[-1], buffer[-1])
        elif x == curses.KEY_BACKSPACE or x == 127: # 127 == Backspace
            if buffer == "":
                continue
            buffer = buffer[:-1]
            state = state[:-6]
        elif x == 27: # 27 = Esc
            break
        elif x == curses.KEY_ENTER or x in [10, 13]: # 10 == '\n', 13 == '\r'
            buffer = ""
            state = " A"
            pass
        pad.clear()
        pad.addstr(0, 0, f"Input: ")
        pad.attron(curses.color_pair(1))
        pad.addstr(0, 7, buffer)
        pad.attroff(curses.color_pair(1))
        pad.addstr(1, 0, state)
        if state[-1] == 'E':
            pad.addstr(4, 0, "The current input contains '000' & ends with '01'")
        else:
            pad.addstr(4, 0, "The current input does not contains '000' & ends with '01'")
        if len(state) > w-6:
            pad.addnstr(5, 0, "Slow down there buckaroo, too many of states already been processed!", w, curses.A_UNDERLINE | curses.A_REVERSE)
        pad.refresh(0, 0, 2, 0, 11, w)

def l3_iterative(stdscr):
    h, w = stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()
    pad = curses.newpad(100, w)
    flag2 = True
    buffer = ""
    state = " A"
    stdscr.addstr(0, 0, "Insert a binary value (0, 1) to continue, press 'ESC' to go back, press 'Enter' to reset")
    stdscr.refresh()
    while flag2:
        x = stdscr.getch()
        if x in [48, 49]: # 48 == '0' and 49 == '1'
            if len(state) > w-6:
                pass
            else:
                buffer += chr(x)
                state += " --> " + l3_delta(state[-1], buffer[-1])
        elif x == curses.KEY_BACKSPACE or x == 127: # 127 == Backspace
            if buffer == "":
                continue
            buffer = buffer[:-1]
            state = state[:-6]
        elif x == 27: # 27 = Esc
            break
        elif x == curses.KEY_ENTER or x in [10, 13]: # 10 == '\n', 13 == '\r'
            buffer = ""
            state = " A"
            pass
        pad.clear()
        pad.addstr(0, 0, f"Input: ")
        pad.attron(curses.color_pair(1))
        pad.addstr(0, 7, buffer)
        pad.attroff(curses.color_pair(1))
        pad.addstr(1, 0, state)
        if state[-1] == 'E' or state[-1] == 'C':
            pad.addstr(4, 0, "The current input starts & ends with different symbol")
        else:
            pad.addstr(4, 0, "The current input does not starts & ends with different symbol")
        if len(state) > w-6:
            pad.addnstr(5, 0, "Slow down there buckaroo, too many of states already been processed!", w, curses.A_UNDERLINE | curses.A_REVERSE)
        pad.refresh(0, 0, 2, 0, 11, w)

def l4_iterative(stdscr):
    h, w = stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()
    pad = curses.newpad(100, w)
    flag2 = True
    buffer = ""
    state = " A"
    stdscr.addstr(0, 0, "Insert a binary value (0, 1) to continue, press 'ESC' to go back, press 'Enter' to reset")
    stdscr.refresh()
    while flag2:
        x = stdscr.getch()
        if x in [48, 49]: # 48 == '0' and 49 == '1'
            if len(state) > w-6:
                pass
            else:
                buffer += chr(x)
                state += " --> " + l4_delta(state[-1], buffer[-1])
        elif x == curses.KEY_BACKSPACE or x == 127: # 127 == Backspace
            if buffer == "":
                continue
            buffer = buffer[:-1]
            state = state[:-6]
        elif x == 27: # 27 = Esc
            break
        elif x == curses.KEY_ENTER or x in [10, 13]: # 10 == '\n', 13 == '\r'
            buffer = ""
            state = " A"
            pass
        pad.clear()
        pad.addstr(0, 0, f"Input: ")
        pad.attron(curses.color_pair(1))
        pad.addstr(0, 7, buffer)
        pad.attroff(curses.color_pair(1))
        pad.addstr(1, 0, state)
        if state[-1] == 'F' or state[-1] == 'I':
            pad.addstr(4, 0, "The current input starts & ends with identical symbol & contains '101'")
        else:
            pad.addstr(4, 0, "The current input does not starts & ends with identical symbol & contains '101'")
        if len(state) > w-6:
            pad.addnstr(5, 0, "Slow down there buckaroo, too many of states already been processed!", w, curses.A_UNDERLINE | curses.A_REVERSE)
        pad.refresh(0, 0, 2, 0, 11, w)