import curses
from nfa import l1_nfa, l2_nfa, l3_nfa, l4_nfa
from dfa import l1_dfa, l2_dfa, l3_dfa, l4_dfa
from delta_dfa import l1_delta_dfa, l2_delta_dfa, l3_delta_dfa, l4_delta_dfa
from hat_delta_nfa import l1_hat_nfa, l2_hat_nfa, l3_hat_nfa, l4_hat_nfa

def print_menu(stdscr, selected: int, menu: list):
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
        else:
            stdscr.addstr(y, x, title)
    stdscr.addstr(y + 3, w//2 - len("USE ARROW KEYS TO NAVIGATE THE MENU")//2, "USE ARROW KEYS TO NAVIGATE THE MENU", curses.A_UNDERLINE)
    stdscr.addstr(y + 5, w//2 - len("Alert: For the most comfortable experience,")//2, "Alert: For the most comfortable experience,", curses.A_PROTECT)
    stdscr.addstr(y + 6, w//2 - len("Please avoid resizing your terminal window.")//2, "Please avoid resizing your terminal window.", curses.A_PROTECT)
    stdscr.addstr(h - 1, w - 8, "@dash4k")

def lang(stdscr, l):
    accept = {
        1: "The current input starts with '10' & ends with '01'",
        2: "The current input contains '000' & ends with '1'",
        3: "The current input starts & ends with different symbol",
        4: "The current input starts & ends with identical symbol & contains '101'"
    }
    reject = {
        1: "The current input does not starts with '10' & ends with '01'",
        2: "The current input does not contains '000' & ends with '1'",
        3: "The current input does not starts & ends with different symbol",
        4: "The current input does not starts & ends with identical symbol & contains '101'"
    }
    h, w = stdscr.getmaxyx()
    stat = 15
    message = 17
    stdscr.clear()
    pad = curses.newpad(100, w)
    flag2 = True
    buffer = ""
    state_dfa = " A"
    nfa = [{'A'}]
    state_nfa = " {'A'}"
    stdscr.addstr(0, 0, "Insert a binary value (0, 1) to continue, press 'Backspace' to erase, press 'Enter' to reset, press 'ESC' to go back.")
    stdscr.refresh()
    while flag2:
        x = stdscr.getch()
        if x in [48, 49]: # 48 == '0' and 49 == '1'
            if len(state_dfa) > w+w:
                pass
            else:
                buffer += chr(x)
                if l == 1:
                    state_dfa += f" --{chr(x)}-> " + l1_delta_dfa(state_dfa[-1], buffer[-1])
                    nfa.append(l1_hat_nfa(nfa[-1], buffer[-1]))
                elif l == 2:
                    state_dfa += f" --{chr(x)}-> " + l2_delta_dfa(state_dfa[-1], buffer[-1])
                    nfa.append(l2_hat_nfa(nfa[-1], buffer[-1]))
                elif l == 3:
                    state_dfa += f" --{chr(x)}-> " + l3_delta_dfa(state_dfa[-1], buffer[-1])
                    nfa.append(l3_hat_nfa(nfa[-1], buffer[-1]))
                elif l == 4:
                    state_dfa += f" --{chr(x)}-> " + l4_delta_dfa(state_dfa[-1], buffer[-1])
                    nfa.append(l4_hat_nfa(nfa[-1], buffer[-1]))
                if nfa[-1] == set():
                    state_nfa += f" --{chr(x)}-> " + str({})    
                else:
                    state_nfa += f" --{chr(x)}-> " + str(nfa[-1])
        elif x == curses.KEY_BACKSPACE or x == 127: # 127 == Backspace
            if buffer == "":
                continue
            buffer = buffer[:-1]
            state_dfa = state_dfa[:-8]
            i = -1
            while True:
                if state_nfa[i] == '{':
                    break
                i -= 1
            i -= 7
            state_nfa = state_nfa[:i]
            nfa = nfa[:-1]
        elif x == 27: # 27 = Esc
            break
        elif x == curses.KEY_ENTER or x in [10, 13]: # 10 == '\n', 13 == '\r'
            buffer = ""
            state_dfa = " A"
            nfa = [{'A'}]
            state_nfa = " {'A'}"
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
        dfa_status = False
        nfa_status = False
        if l == 1:
            if l1_dfa(buffer):
                dfa_status = True
                pad.addstr(stat, 12, " ACCEPTED ", curses.A_REVERSE)
            else:
                pad.addstr(stat, 12, " REJECTED ", curses.A_REVERSE)
            if l1_nfa(buffer):
                nfa_status = True
                pad.addstr(stat, 37, " ACCEPTED ", curses.A_REVERSE)
            else:
                pad.addstr(stat, 37, " REJECTED ", curses.A_REVERSE)
        elif l == 2:
            if l2_dfa(buffer):
                dfa_status = True
                pad.addstr(stat, 12, " ACCEPTED ", curses.A_REVERSE)
            else:
                pad.addstr(stat, 12, " REJECTED ", curses.A_REVERSE)
            if l2_nfa(buffer):
                nfa_status = True
                pad.addstr(stat, 37, " ACCEPTED ", curses.A_REVERSE)
            else:
                pad.addstr(stat, 37, " REJECTED ", curses.A_REVERSE)
        elif l == 3:
            if l3_dfa(buffer):
                dfa_status = True
                pad.addstr(stat, 12, " ACCEPTED ", curses.A_REVERSE)
            else:
                pad.addstr(stat, 12, " REJECTED ", curses.A_REVERSE)
            if l3_nfa(buffer):
                nfa_status = True
                pad.addstr(stat, 37, " ACCEPTED ", curses.A_REVERSE)
            else:
                pad.addstr(stat, 37, " REJECTED ", curses.A_REVERSE)
        elif l == 4:
            if l4_dfa(buffer):
                dfa_status = True
                pad.addstr(stat, 12, " ACCEPTED ", curses.A_REVERSE)
            else:
                pad.addstr(stat, 12, " REJECTED ", curses.A_REVERSE)
            if l4_nfa(buffer):
                nfa_status = True
                pad.addstr(stat, 37, " ACCEPTED ", curses.A_REVERSE)
            else:
                pad.addstr(stat, 37, " REJECTED ", curses.A_REVERSE)
        if dfa_status and nfa_status:
            pad.addstr(message, 0, accept[l], curses.A_BOLD)
        else:
            pad.addstr(message, 0, reject[l], curses.A_BOLD)
        if len(state_dfa) > w+w:
            pad.addnstr(19, 0, "Slow down there buckaroo, too many of the states have already been processed!", w, curses.A_UNDERLINE | curses.A_ITALIC | curses.A_BOLD)
        pad.refresh(0, 0, 2, 0, 25, w)