import curses

def print_menu(stdscr, selected: int, menu: list, nfa_initialized: bool):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.addstr(h//2 - len(menu)//2 - 5, w//2 - len("DETERMINISTIC FINITE AUTOMATA")//2, "DETERMINISTIC FINITE AUTOMATA", curses.A_BOLD)
    for i, title in enumerate(menu):
        x = w//2 - len(title)//2
        y = h//2 - len(menu)//2 - 2 + i
        if i == selected:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x - 4, "--> " + title)
            stdscr.attroff(curses.color_pair(1))
        elif i == 0 and nfa_initialized:
            stdscr.addstr(y, x, title, curses.A_DIM)
        elif i < 4 and i > 0 and not nfa_initialized:
            stdscr.addstr(y, x, title, curses.A_DIM)
        else:
            stdscr.addstr(y, x, title)
    stdscr.addstr(y + 3, w//2 - len("USE ARROW KEYS TO NAVIGATE THE MENU")//2, "USE ARROW KEYS TO NAVIGATE THE MENU", curses.A_UNDERLINE)
    stdscr.addstr(y + 5, w//2 - len("Alert: For the most comfortable experience,")//2, "Alert: For the most comfortable experience,", curses.A_PROTECT)
    stdscr.addstr(y + 6, w//2 - len("Please avoid resizing your terminal window.")//2, "Please avoid resizing your terminal window.", curses.A_PROTECT)
    stdscr.addstr(h - 1, w - 8, "@dash4k")

def Initialize_nfa(stdscr) -> bool:
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    states_buffer = " "
    language_buffer = []
    row = 0
    stdscr.addstr(0, 0, "Initialize NFA", curses.A_BOLD)
    stdscr.addstr(2, 0, "Number of state(s)         :", curses.A_UNDERLINE)
    stdscr.addstr(2, 29, states_buffer, curses.A_REVERSE)
    stdscr.addstr(3, 0, "(Enter an integer value > 0)", curses.A_DIM)
    stdscr.addstr(6, 0, "Language                   :", curses.A_UNDERLINE)
    stdscr.addstr(6, 29, str(language_buffer))
    stdscr.addstr(7, 0, "(Enter language character(s))", curses.A_DIM)
    stdscr.addstr(15, w-10, " NEXT ", curses.color_pair(1))
    stdscr.addstr(15, w-20, " BACK ", curses.color_pair(2))
    stdscr.addstr(h - 1, w - 8, "@dash4k")
    pad = curses.newpad(100, w)
    while True:
        x = stdscr.getch()
        if row == 0:
            if x in [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]:
                if states_buffer == " ":
                    states_buffer = ""
                elif len(states_buffer) == 3:
                    pass
                else:
                    states_buffer += chr(x)
        elif row == 1:
            if chr(x).isalnum() and x != curses.KEY_UP and x != curses.KEY_DOWN and x != 127 and x != curses.KEY_BACKSPACE and x not in [10, 13] and chr(x) not in language_buffer:
                language_buffer.append(chr(x))
        if x == 27: # 27 = Esc
            return False
        elif x == curses.KEY_ENTER or x in [10, 13]: # 10 == '\n', 13 == '\r'
            # To Do: Benerin nih!
            if row == 3:
                return False
            elif row == 2:
                return True
        elif x == curses.KEY_BACKSPACE or x == 127: # 127 == Backspace
            if row == 0:
                if states_buffer == " ":
                    continue
                elif len(states_buffer) == 1:
                    states_buffer = " "
                else:
                    states_buffer = states_buffer[:-1]
            elif row == 1:
                if language_buffer == {}:
                    continue
                language_buffer = language_buffer[:-1]
        elif x == curses.KEY_UP:
            if row > 0:
                row -= 1
            else:
                row = 3
        elif x == curses.KEY_DOWN:
            if row < 3:
                row += 1
            else:
                row = 0
        pad.clear()
        pad.addstr(0, 0, "Number of state(s)         :", curses.A_UNDERLINE)
        pad.addstr(1, 0, "(Enter an integer value > 0)", curses.A_DIM)
        pad.addstr(4, 0, "Language                   :", curses.A_UNDERLINE)
        pad.addstr(5, 0, "(Enter language character(s))", curses.A_DIM)
        pad.addstr(13, w-10, " NEXT ", curses.color_pair(1))
        pad.addstr(13, w-20, " BACK ", curses.color_pair(2))
        if row == 0:
            pad.addstr(0, 29, states_buffer, curses.A_REVERSE)
            pad.addstr(4, 29, str(language_buffer))
        elif row == 1:
            pad.addstr(0, 29, states_buffer)
            pad.addstr(4, 29, str(language_buffer), curses.A_REVERSE)
        elif row == 2:
            pad.addstr(0, 29, states_buffer)
            pad.addstr(4, 29, str(language_buffer))
            pad.addstr(13, w-10, " NEXT ", curses.color_pair(1) | curses.A_REVERSE)
        elif row == 3:
            pad.addstr(0, 29, states_buffer)
            pad.addstr(4, 29, str(language_buffer))
            pad.addstr(13, w-20, " BACK ", curses.color_pair(2) | curses.A_REVERSE)
        pad.refresh(0, 0, 2, 0, 20, w)