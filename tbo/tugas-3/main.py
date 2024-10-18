# from nfa import nfa
# from dfa import dfa
# from convert import states, finals, deltas, simplified

# # nfa_finals = {
# #     'E'
# # }

# # delta_nfa = {
# #     ('A', '1'): {'B'},
# #     ('B', '0'): {'C'},
# #     ('C', '0'): {'C', 'D'},
# #     ('C', '1'): {'C'},
# #     ('D', '1'): {'E'}
# # }

# # # print("True") if nfa(nfa_finals, delta_nfa, "100100", {'A'}) else print("False")

# # nfa_states = {chr(i) for i in range(65, 70)}

# # # print(states(nfa_states))

# # # print(finals(nfa_finals, states(nfa_states)))

# # delta_dfa = deltas(delta_nfa, states(nfa_states), {'0', '1'}, 'A')


# # # print(delta_dfa)

# # # print("True") if dfa(finals(nfa_finals, states(nfa_states)), delta_dfa, "1001", frozenset({'A'})) else print("False")

# # for key, value in delta_dfa.items():
# #     print(f"{key}: {value}")

# # print()

# # print(finals(nfa_finals, states(nfa_states)))

# # s_delta_dfa = simplified(delta_dfa) 

# # print()

# # print(s_delta_dfa)

# # result = dfa(finals(nfa_finals, states(nfa_states)), s_delta_dfa, "10010001", 'A')
# # print()
# # print(result)

from util import print_menu, Initialize_nfa
import curses

def main(stdscr):
    menu = [
        "Initialize NFA", 
        "Convert NFA to DFA", 
        "NFA", 
        "DFA", 
        "EXIT PROGRAM"
        ]
    curses.curs_set(0) #cursor visibility
    row = 0
    flag1 = True
    nfa_initialized = False
    
    print_menu(stdscr, row, menu, nfa_initialized)

    while flag1:
        key = stdscr.getch()
        if key == curses.KEY_UP:
            if row > 0:
                if nfa_initialized and row == 1:
                    row = 4
                elif not nfa_initialized:
                    row = 1
                else:
                    row -= 1
            else:
                row = 4
        elif key == curses.KEY_DOWN:
            if row < 4:
                if nfa_initialized:
                    row += 1
                else:
                    row = 4
            else:
                if not nfa_initialized:
                    row = 0
                else:
                    row = 1
        elif key == curses.KEY_ENTER or key in [10, 13]: # 10 == '\n', 13 == '\r'    
            if row == 4:
                flag1 = False
            else:
                if row == 0:
                    # lang(stdscr, 1)
                    if Initialize_nfa(stdscr):
                        nfa_initialized = True
                        row = 1
                elif row == 1:
                    # lang(stdscr, 2)
                    pass
                elif row == 2:
                    # lang(stdscr, 3)
                    pass
                elif row == 3:
                    # lang(stdscr, 4)
                    pass
            pass
        print_menu(stdscr, row, menu, nfa_initialized)

curses.wrapper(main)