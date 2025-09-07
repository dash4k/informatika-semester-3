from util import print_menu, initialize_nfa, convert_menu, lang
import curses

def main(stdscr):
    menu = [
        "Initialize NFA", 
        "Convert NFA to DFA", 
        "NFA & NFA", 
        "RESET", 
        "EXIT PROGRAM"
        ]
    curses.curs_set(0) #cursor visibility
    row = 0
    flag1 = True
    nfa_initialized = False
    dfa_initialized = False
    nfa_states = set()
    dfa_states = set()
    nfa_language = set()
    dfa_language = set()
    delta_nfa = {}
    delta_dfa = {}
    nfa_q0 = set()
    dfa_q0 = ""
    nfa_finals = set()
    dfa_finals = set()
    nfa_list = []
    
    print_menu(stdscr, row, menu, nfa_initialized, dfa_initialized)

    while flag1:
        key = stdscr.getch()
        if key == curses.KEY_UP:
            if not nfa_initialized:
                if row > 0:
                    row = 0
                else:
                    row = 4
            elif not dfa_initialized:
                if row > 1:
                    row = 1
                else:
                    row = 4
            else:
                if 2 < row <= 4:
                    row -= 1
                else:
                    row = 4
        elif key == curses.KEY_DOWN:
            if not nfa_initialized:
                if row > 0:
                    row = 0
                else:
                    row = 4
            elif not dfa_initialized:
                if row > 1:
                    row = 1
                else:
                    row = 4
            else:
                if 2 <= row < 4:
                    row += 1
                else:
                    row = 2
        elif key == curses.KEY_ENTER or key in [10, 13]: # 10 == '\n', 13 == '\r'    
            if row == 4:
                flag1 = False
            else:
                if row == 0:
                    nfa_states, nfa_language, delta_nfa, nfa_q0, nfa_finals, nfa_initialized = initialize_nfa(stdscr)
                    nfa_list.append(nfa_states)
                    nfa_list.append(nfa_language)
                    nfa_list.append(delta_nfa)
                    nfa_list.append(nfa_q0)
                    nfa_list.append(nfa_finals)
                    if nfa_initialized:
                        row = 1
                elif row == 1:
                    dfa_states, dfa_language, delta_dfa, dfa_q0, dfa_finals, dfa_initialized = convert_menu(stdscr, nfa_list)
                    if dfa_initialized:
                        row = 2
                elif row == 2:
                    lang(stdscr, delta_dfa, delta_nfa, nfa_finals, dfa_finals, nfa_language)
                elif row == 3:
                    row = 0
                    flag1 = True
                    nfa_initialized = False
                    dfa_initialized = False
                    nfa_states = set()
                    dfa_states = set()
                    nfa_language = set()
                    dfa_language = set()
                    delta_nfa = {}
                    delta_dfa = {}
                    nfa_q0 = set()
                    dfa_q0 = ""
                    nfa_finals = set()
                    dfa_finals = set()
                    nfa_list = []
            pass
        print_menu(stdscr, row, menu, nfa_initialized, dfa_initialized)

curses.wrapper(main)