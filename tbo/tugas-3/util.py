import curses
from convert import states, finals, deltas, simplified
from nfa import l_nfa, hat_delta_nfa
from dfa import dfa

def print_menu(stdscr, selected: int, menu: list, nfa_initialized: bool, dfa_initialized: bool):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.addstr(h//2 - len(menu)//2 - 5, w//2 - len("DETERMINISTIC FINITE AUTOMATA")//2, "DETERMINISTIC FINITE AUTOMATA", curses.A_BOLD)
    for i, title in enumerate(menu):
        x = w//2 - len(title)//2
        y = h//2 - len(menu)//2 - 2 + i
        if i == selected:
            stdscr.addstr(y, x, title, curses.A_REVERSE)
        elif not nfa_initialized and 0 < i < 4:
            stdscr.addstr(y, x, title, curses.A_DIM)
        elif not dfa_initialized and nfa_initialized and i != 1 and i != 4:
            stdscr.addstr(y, x, title, curses.A_DIM)
        elif dfa_initialized and nfa_initialized:
            if i < 2:
                stdscr.addstr(y, x, title, curses.A_DIM)
            else:
                stdscr.addstr(y, x, title)
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
    language_buffer = []
    states = set()
    row1 = 0
    stdscr.addstr(0, 0, "Initialize NFA", curses.A_BOLD)
    stdscr.addstr(4, 0, "Number of state(s)         :", curses.A_UNDERLINE)
    stdscr.addstr(4, 29, states_buffer, curses.A_REVERSE)
    stdscr.addstr(5, 0, "(Enter an integer 0 < x < 8)", curses.A_DIM)
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
                elif len(states_buffer) == 1:
                    states_buffer = "7"
                else:
                    states_buffer += chr(x)
                    if int(states_buffer) > 7:
                        states_buffer = "7"
        elif row1 == 1:
            if chr(x).isalnum() and x != curses.KEY_UP and x != curses.KEY_DOWN and x != 127 and x != curses.KEY_BACKSPACE and x not in [10, 13] and chr(x) not in language_buffer:
                language_buffer.append(chr(x))
        if x == 27: # 27 = Esc
            return set(), set(), {}, set(), set(), False
        elif x == curses.KEY_ENTER or x in [10, 13]: # 10 == '\n', 13 == '\r'
            if row1 == 2:
                if states_buffer != " " and language_buffer != []:
                    state_buffer = " "
                    sigma_buffer = " "
                    transition_buffer = " "
                    transition_set = []
                    finals_buffer = []
                    delta_nfa = {}
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
                                if delta_nfa != {} and language_buffer != [] and finals_buffer != [] and states != set():
                                    return states, set(language_buffer), delta_nfa, {'A'}, set(finals_buffer), True
                                else:
                                    pass
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
                else:
                    pass
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

def convert_menu(stdscr, nfa_list: list):
    nfa_titles = [
        "NFA States   :",
        "NFA Languages:",
        "Delta NFA    :",
        "NFA q0       :",
        "NFA Finals   :"
    ]
    dfa_titles = [
        "DFA States            :",
        "DFA Languages         :",
        "Delta DFA             :",
        "Delta DFA (Simplified):",
        "DFA q0                :",
        "DFA Finals            :"
    ]
    dfa_states = states(nfa_list[0])
    dfa_language = nfa_list[1]
    delta_dfa = deltas(nfa_list[2], dfa_states, dfa_language, nfa_list[3])
    s_delta_dfa = simplified(delta_dfa)
    dfa_q0 = str(nfa_list[3])
    dfa_finals = finals(nfa_list[4], dfa_states)
    dfa_list = []
    dfa_list.append(dfa_states)
    dfa_list.append(dfa_language)
    dfa_list.append(delta_dfa)
    dfa_list.append(s_delta_dfa)
    dfa_list.append(dfa_q0)
    dfa_list.append(dfa_finals)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.addstr(0, 0, "Convert NFA to DFA", curses.A_BOLD)
    stdscr.addstr(3, 0, "NFA", curses.A_REVERSE)
    pad = curses.newpad(100, w)
    i = row1 = 0
    for title in nfa_titles:
        y, x = stdscr.getyx()
        stdscr.addstr(y + 2, 0, title, curses.A_UNDERLINE)
        stdscr.addstr(y + 3, 0, str(nfa_list[i]))
        i += 1
    stdscr.addstr(h-5, w-10, " NEXT ", curses.color_pair(1))
    h, w = stdscr.getmaxyx()
    while True:
        pad.clear()
        if row1 == 0:
            pad.addstr(0, w-10, " NEXT ", curses.color_pair(1) | curses.A_REVERSE)
        elif row1 == 1:
            pad.addstr(0, w-10, " NEXT ", curses.color_pair(1))
        x = stdscr.getch()
        if x == 27: # 27 = Esc
            return set(), set(), {}, "", set(), False 
        elif x == curses.KEY_UP or x == curses.KEY_RIGHT:
            if row1 > 0:
                row1 -= 1
            else:
                row1 = 1
        elif x == curses.KEY_DOWN or x == curses.KEY_LEFT:
            if row1 < 1:
                row1 += 1
            else:
                row1 = 0
        elif x == curses.KEY_ENTER or x in [10, 13]: # 10 == '\n', 13 == '\r'
            if row1 == 1:
                stdscr.clear()
                stdscr.addstr(0, 0, "Convert NFA to DFA", curses.A_BOLD)
                stdscr.addstr(3, 0, "DFA", curses.A_REVERSE)
                j = row2 = 0
                for title in dfa_titles[:-3]:
                    y, x = stdscr.getyx()
                    stdscr.addstr(y + 2, 0, title, curses.A_UNDERLINE)
                    stdscr.addstr(y + 3, 0, str(dfa_list[j]))
                    j += 1
                stdscr.addstr(h-5, w-10, " NEXT ", curses.color_pair(1))
                while True:
                    pad.clear()
                    if row2 == 0:
                        pad.addstr(0, w-10, " NEXT ", curses.color_pair(1) | curses.A_REVERSE)
                    elif row2 == 1:
                        pad.addstr(0, w-10, " NEXT ", curses.color_pair(1))
                    z = stdscr.getch()
                    if z == 27: # 27 = Esc
                        return set(), set(), {}, "", set(), False
                    elif z == curses.KEY_UP or z == curses.KEY_RIGHT:
                        if row2 > 0:
                            row2 -= 1
                        else:
                            row2 = 1
                    elif z == curses.KEY_DOWN or z == curses.KEY_LEFT:
                        if row2 < 1:
                            row2 += 1
                        else:
                            row2 = 0
                    elif z == curses.KEY_ENTER or z in [10, 13]: # 10 == '\n', 13 == '\r'
                        if row2 == 1:
                            stdscr.clear()
                            stdscr.addstr(0, 0, "Convert NFA to DFA", curses.A_BOLD)
                            stdscr.addstr(3, 0, "DFA", curses.A_REVERSE)
                            row3 = 0
                            k = 3
                            for title in dfa_titles[-3:]:
                                y, x = stdscr.getyx()
                                stdscr.addstr(y + 2, 0, title, curses.A_UNDERLINE)
                                stdscr.addstr(y + 3, 0, str(dfa_list[k]))
                                k += 1
                            stdscr.addstr(h-5, w-10, " NEXT ", curses.color_pair(1))
                            while True:
                                pad.clear()
                                if row3 == 0:
                                    pad.addstr(0, w-10, " NEXT ", curses.color_pair(1) | curses.A_REVERSE)
                                elif row3 == 1:
                                    pad.addstr(0, w-10, " NEXT ", curses.color_pair(1))
                                p = stdscr.getch()
                                if p == 27: # 27 = Esc
                                    return set(), set(), {}, "", set(), False
                                elif p == curses.KEY_UP or p == curses.KEY_RIGHT:
                                    if row3 > 0:
                                        row3 -= 1
                                    else:
                                        row3 = 1
                                elif p == curses.KEY_DOWN or p == curses.KEY_LEFT:
                                    if row3 < 1:
                                        row3 += 1
                                    else:
                                        row3 = 0
                                elif p == curses.KEY_ENTER or p in [10, 13]: # 10 == '\n', 13 == '\r'
                                    if row3 == 1:
                                        return dfa_states, dfa_language, s_delta_dfa, dfa_q0, dfa_finals, True
                                    else:
                                        pass
                                pad.refresh(0, 0, h-5, 0, h-5, w)
                        else:
                            pass
                    pad.refresh(0, 0, h-5, 0, h-5, w)
                else:
                    pass
        pad.refresh(0, 0, h-5, 0, h-5, w)

def lang(stdscr, delta_dfa: dict, delta_nfa: dict, nfa_finals: set, dfa_finals: set, language: set):
    h, w = stdscr.getmaxyx()
    stat = 13
    message = 15
    stdscr.clear()
    pad = curses.newpad(100, w)
    flag2 = True
    buffer = ""
    state_dfa = " A"
    l_dfa = ['A']
    nfa = [{'A'}]
    state_nfa = " {'A'}"
    stdscr.addstr(0, 0, "Insert a language character to continue, press 'Backspace' to erase, press 'Enter' to reset, press 'ESC' to go back.")
    stdscr.addstr(h - 1, w - 8, "@dash4k")
    stdscr.refresh()
    while flag2:
        x = stdscr.getch()
        if chr(x) in language:
            if len(state_dfa) > w+w:
                pass
            else:
                buffer += chr(x)
                # fix for 'Dead' state cause only 'd' is inputted
                l_dfa.append(delta_dfa[(l_dfa[-1], buffer[-1])])
                # if l_dfa[-4:] == "Dead":
                #     state_dfa += f" --{chr(x)}-> " + delta_dfa[("Dead", buffer[-1])]
                # else:    
                #     state_dfa += f" --{chr(x)}-> " + delta_dfa[(state_dfa[-1], buffer[-1])]
                state_dfa += f" --{chr(x)}-> " + l_dfa[-1]
                nfa.append(hat_delta_nfa(delta_nfa, nfa[-1], buffer[-1]))
                if nfa[-1] == set():
                    state_nfa += f" --{chr(x)}-> " + str({})    
                else:
                    state_nfa += f" --{chr(x)}-> " + str(nfa[-1])
        elif x == curses.KEY_BACKSPACE or x == 127: # 127 == Backspace
            if buffer == "":
                continue
            buffer = buffer[:-1]
            if state_dfa[-4:] == "Dead":
                state_dfa = state_dfa[:-11]
            else:
                state_dfa = state_dfa[:-8]
            i = -1
            while True:
                if state_nfa[i] == '{':
                    break
                i -= 1
            i -= 7
            state_nfa = state_nfa[:i]
            nfa = nfa[:-1]
            l_dfa = l_dfa[:-1]
        elif x == 27: # 27 = Esc
            break
        elif x == curses.KEY_ENTER or x in [10, 13]: # 10 == '\n', 13 == '\r'
            buffer = ""
            state_dfa = " A"
            nfa = [{'A'}]
            state_nfa = " {'A'}"
            l_dfa = ['A']
            pass
        pad.clear()
        pad.addstr(0, 0, f"Input: ")
        pad.addstr(0, 7, buffer, curses.A_REVERSE)
        pad.addstr(2, 0, "DFA States:", curses.A_BOLD)
        pad.addstr(3, 0, state_dfa)
        pad.addstr(7, 0, "NFA States:", curses.A_BOLD)
        pad.addstr(8, 0, state_nfa)
        pad.addstr(stat, 0, "DFA Status: ", curses.A_ITALIC)
        pad.addstr(stat, 25, "NFA Status: ", curses.A_ITALIC)
        if dfa(dfa_finals, delta_dfa, buffer, 'A'):
            pad.addstr(stat, 12, " ACCEPTED ", curses.A_REVERSE)
        else:
            pad.addstr(stat, 12, " REJECTED ", curses.A_REVERSE)
        if l_nfa(nfa_finals, delta_nfa, buffer, {'A'}):
            pad.addstr(stat, 37, " ACCEPTED ", curses.A_REVERSE)
        else:
            pad.addstr(stat, 37, " REJECTED ", curses.A_REVERSE)
        if len(state_dfa) > w+w:
            pad.addnstr(message, 0, "Slow down there buckaroo, too many of the states have already been processed!", w, curses.A_UNDERLINE | curses.A_ITALIC | curses.A_BOLD)
        pad.refresh(0, 0, 2, 0, 25, w)