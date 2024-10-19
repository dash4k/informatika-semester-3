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

def initialize_nfa(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    states_buffer = " "
    state_buffer = " "
    sigma_buffer = " "
    transition_buffer = " "
    transition_set = []
    language_buffer = []
    states = set()
    finals_buffer = []
    delta_nfa = {}
    row1 = 0
    stdscr.addstr(0, 0, "Initialize NFA", curses.A_BOLD)
    stdscr.addstr(4, 0, "Number of state(s)         :", curses.A_UNDERLINE)
    stdscr.addstr(4, 29, states_buffer, curses.A_REVERSE)
    stdscr.addstr(5, 0, "(Enter an integer 0 < x < 24)", curses.A_DIM)
    stdscr.addstr(8, 0, "Language                   :", curses.A_UNDERLINE)
    stdscr.addstr(8, 29, str(language_buffer))
    stdscr.addstr(9, 0, "(Enter language character(s))", curses.A_DIM)
    stdscr.addstr(15, w-10, " NEXT ", curses.color_pair(1))
    stdscr.addstr(15, w-20, " BACK ", curses.color_pair(2))
    stdscr.addstr(h - 1, w - 8, "@dash4k")
    pad = curses.newpad(100, w)
    while True:
        x = stdscr.getch()
        if row1 == 0:
            if x in [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]:
                if states_buffer == " ":
                    if x == 48:
                        pass
                    else:
                        states_buffer = ""
                        states_buffer += chr(x)
                elif len(states_buffer) == 2:
                    states_buffer = "24"
                else:
                    states_buffer += chr(x)
                    if int(states_buffer) > 24:
                        states_buffer = "24"
        elif row1 == 1:
            if chr(x).isalnum() and x != curses.KEY_UP and x != curses.KEY_DOWN and x != 127 and x != curses.KEY_BACKSPACE and x not in [10, 13] and chr(x) not in language_buffer:
                language_buffer.append(chr(x))
        if x == 27: # 27 = Esc
            return False
        elif x == curses.KEY_ENTER or x in [10, 13]: # 10 == '\n', 13 == '\r'
            if row1 == 2:
                row2 = 0
                for i in range(65, 65+int(states_buffer)):
                    states.update(chr(i))
                pad.clear()
                pad.addstr(2, 0, "Current NFA State(s)        :", curses.A_UNDERLINE)
                pad.addstr(2, 31, str(states))
                pad.addstr(2, 41 + len(str(states)), "Current NFA Sigma(s)        :", curses.A_UNDERLINE)
                pad.addstr(2, 72 + len(str(states)), str(language_buffer))
                pad.addstr(5, 0, "Enter the final state(s)    :", curses.A_UNDERLINE)
                pad.addstr(5, 31, str(finals_buffer), curses.A_REVERSE)
                pad.addstr(6, 0, "(Enter language character(s))", curses.A_DIM)
                pad.addstr(9, 0, "Enter the state's transition:")
                pad.addstr(9, 31, f"(")
                pad.addstr(9, 32, f"'{state_buffer}'")
                pad.addstr(9, 35, f", ")
                pad.addstr(9, 38, f"'{sigma_buffer}'")
                pad.addstr(9, 42, f"): ")
                pad.addstr(9, 46, f"'{transition_buffer}'")
                pad.addstr(10, 0, "((State, Sigma): Transition)", curses.A_DIM)
                pad.addstr(11, 0, "  (Press Enter when done)   ", curses.A_DIM)
                pad.addstr(13, w-10, " NEXT ", curses.color_pair(1))
                pad.addstr(13, w-20, " BACK ", curses.color_pair(2))
                pad.addstr(16, 0, "Current Delta NFA           :", curses.A_UNDERLINE)
                pad.addstr(18, 0, str(delta_nfa))
                pad.refresh(0, 0, 2, 0, 20, w)
                while True:
                    y = stdscr.getch()
                    if row2 == 0 and chr(y).isalpha() and chr(y).capitalize() in states and chr(y).capitalize() not in finals_buffer:
                        finals_buffer.append(chr(y).capitalize())
                    elif row2 == 1:
                        if state_buffer == " ": 
                            if chr(y).isalpha() and chr(y).capitalize() in states:
                                state_buffer = ""
                                state_buffer += chr(y).capitalize()
                        elif sigma_buffer == " ":
                            if chr(y) in language_buffer:
                                sigma_buffer = ""
                                sigma_buffer += chr(y)
                            else:
                                pass
                        else:
                            if chr(y).isalpha() and chr(y).capitalize() in states:
                                if transition_buffer == " ":
                                    transition_buffer = ""
                                    transition_buffer += chr(y).capitalize()
                                    transition_set.append(transition_buffer[-1])
                                else:
                                    if chr(y).capitalize() in transition_set:
                                        pass
                                    else:
                                        transition_buffer += f", {chr(y).capitalize()}"
                                        transition_set.append(transition_buffer[-1])
                    if y == 27: # 27 = Esc
                        break
                    elif y == curses.KEY_UP:
                        if row2 > 0:
                            row2 -= 1
                        else:
                            row2 = 3
                    elif y == curses.KEY_DOWN:
                        if row2 < 3:
                            row2 += 1
                        else:
                            row2 = 0
                    elif y == curses.KEY_BACKSPACE or y == 127: # 127 == Backspace
                        if row2 == 0:
                            if finals_buffer == {}:
                                continue
                            finals_buffer = finals_buffer[:-1]
                        elif row2 == 1:
                            if transition_buffer != " ":
                                if len(transition_buffer) > 1:
                                    transition_buffer = transition_buffer[:-3]
                                    transition_set.pop()
                                else:
                                    transition_buffer = " "
                                    transition_set = []
                            elif sigma_buffer != " ":
                                sigma_buffer = " "
                            elif state_buffer != " ":
                                state_buffer = " "
                            else:
                                pass
                    elif (y == curses.KEY_ENTER or y in [10, 13]):
                        if row2 == 1:
                            if state_buffer != " " and sigma_buffer != " " and transition_buffer != " ":
                                delta_nfa[(state_buffer, sigma_buffer)] = set(transition_set)
                                state_buffer = " "
                                sigma_buffer = " "
                                transition_buffer = " "
                                transition_set = []
                        elif row2 == 2:
                            return states, set(language_buffer), delta_nfa, {'A'}, set(finals_buffer), True
                        elif row2 == 3:
                            break
                    pad.clear()
                    pad.addstr(2, 41 + len(str(states)), "Current NFA Sigma(s)        :", curses.A_UNDERLINE)
                    pad.addstr(2, 72 + len(str(states)), str(language_buffer))
                    pad.addstr(2, 0, "Current NFA State(s)        :", curses.A_UNDERLINE)
                    pad.addstr(2, 31, str(states))
                    pad.addstr(5, 0, "Enter the final state(s)    :", curses.A_UNDERLINE)
                    pad.addstr(6, 0, "(Enter language character(s))", curses.A_DIM)
                    pad.addstr(9, 0, "Enter the state's transition:")
                    pad.addstr(10, 0, "((State, Sigma): Transition)", curses.A_DIM)
                    pad.addstr(11, 0, "  (Press Enter when done)   ", curses.A_DIM)
                    pad.addstr(13, w-10, " NEXT ", curses.color_pair(1))
                    pad.addstr(13, w-20, " BACK ", curses.color_pair(2))
                    pad.addstr(16, 0, "Current Delta NFA           :", curses.A_UNDERLINE)
                    pad.addstr(18, 0, str(delta_nfa))
                    if row2 == 0:
                        pad.addstr(5, 31, str(finals_buffer), curses.A_REVERSE)
                        pad.addstr(9, 31, f"(")
                        pad.addstr(9, 32, f"'{state_buffer}'")
                        pad.addstr(9, 35, f", ")
                        pad.addstr(9, 38, f"'{sigma_buffer}'")
                        pad.addstr(9, 42, f"): ")
                        pad.addstr(9, 46, f"'{transition_buffer}'")
                    elif row2 == 1:
                        pad.addstr(5, 31, str(finals_buffer))
                        pad.addstr(9, 31, f"(")
                        pad.addstr(9, 35, f", ")
                        pad.addstr(9, 42, f"): ")
                        if state_buffer == " ":
                            pad.addstr(9, 32, f"'{state_buffer}'", curses.A_REVERSE)
                            pad.addstr(9, 38, f"'{sigma_buffer}'")
                            pad.addstr(9, 46, f"'{transition_buffer}'")
                        elif sigma_buffer == " ":
                            pad.addstr(9, 32, f"'{state_buffer}'")
                            pad.addstr(9, 38, f"'{sigma_buffer}'", curses.A_REVERSE)
                            pad.addstr(9, 46, f"'{transition_buffer}'")
                        else:
                            pad.addstr(9, 32, f"'{state_buffer}'")
                            pad.addstr(9, 38, f"'{sigma_buffer}'")
                            pad.addstr(9, 46, f"'{transition_buffer}'", curses.A_REVERSE)
                    elif row2 == 2:
                        pad.addstr(9, 31, f"(")
                        pad.addstr(9, 32, f"'{state_buffer}'")
                        pad.addstr(9, 35, f", ")
                        pad.addstr(9, 38, f"'{sigma_buffer}'")
                        pad.addstr(9, 42, f"): ")
                        pad.addstr(9, 46, f"'{transition_buffer}'")
                        pad.addstr(5, 31, str(finals_buffer))
                        pad.addstr(13, w-10, " NEXT ", curses.color_pair(1) | curses.A_REVERSE)
                    elif row2 == 3:
                        pad.addstr(9, 31, f"(")
                        pad.addstr(9, 32, f"'{state_buffer}'")
                        pad.addstr(9, 35, f", ")
                        pad.addstr(9, 38, f"'{sigma_buffer}'")
                        pad.addstr(9, 42, f"): ")
                        pad.addstr(9, 46, f"'{transition_buffer}'")
                        pad.addstr(5, 31, str(finals_buffer))
                        pad.addstr(13, w-20, " BACK ", curses.color_pair(2) | curses.A_REVERSE)
                    pad.refresh(0, 0, 2, 0, 20, w)
            elif row1 == 3:
                # states, set(language_buffer), delta_nfa, {'A'}, set(finals_buffer), True
                return set(), set(), {}, set(), set(), False
        elif x == curses.KEY_BACKSPACE or x == 127: # 127 == Backspace
            if row1 == 0:
                if states_buffer == " ":
                    continue
                elif len(states_buffer) == 1:
                    states_buffer = " "
                else:
                    states_buffer = states_buffer[:-1]
            elif row1 == 1:
                if language_buffer == {}:
                    continue
                language_buffer = language_buffer[:-1]
        elif x == curses.KEY_UP:
            if row1 > 0:
                row1 -= 1
            else:
                row1 = 3
        elif x == curses.KEY_DOWN:
            if row1 < 3:
                row1 += 1
            else:
                row1 = 0
        pad.clear()
        pad.addstr(2, 0, "Number of state(s)         :", curses.A_UNDERLINE)
        pad.addstr(3, 0, "(Enter an integer 0 < x < 24)", curses.A_DIM)
        pad.addstr(6, 0, "Language                   :", curses.A_UNDERLINE)
        pad.addstr(7, 0, "(Enter language character(s))", curses.A_DIM)
        pad.addstr(13, w-10, " NEXT ", curses.color_pair(1))
        pad.addstr(13, w-20, " BACK ", curses.color_pair(2))
        if row1 == 0:
            pad.addstr(2, 29, states_buffer, curses.A_REVERSE)
            pad.addstr(6, 29, str(language_buffer))
        elif row1 == 1:
            pad.addstr(2, 29, states_buffer)
            pad.addstr(6, 29, str(language_buffer), curses.A_REVERSE)
        elif row1 == 2:
            pad.addstr(2, 29, states_buffer)
            pad.addstr(6, 29, str(language_buffer))
            pad.addstr(13, w-10, " NEXT ", curses.color_pair(1) | curses.A_REVERSE)
        elif row1 == 3:
            pad.addstr(2, 29, states_buffer)
            pad.addstr(6, 29, str(language_buffer))
            pad.addstr(13, w-20, " BACK ", curses.color_pair(2) | curses.A_REVERSE)
        pad.refresh(0, 0, 2, 0, 20, w)

def convert_menu(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.addstr(0, 0, "Convert NFA to DFA", curses.A_BOLD)