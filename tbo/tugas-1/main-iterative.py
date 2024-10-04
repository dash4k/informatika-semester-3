from delta_dfa import l1_delta, l2_delta, l3_delta, l4_delta
from util import print_menu, l1_iterative, l2_iterative, l3_iterative
import curses

def main(stdscr):
    menu = [
        "1. L1 (Starts with '10' & ends with '01')", 
        "2. L2 (Contains '000' & ends with '01')", 
        "3. L3 (Starts & ends with different symbol)", 
        "4. L4 (Starts & ends with same symbol & contains '101')", 
        "5. Exit"
        ]
    curses.curs_set(0) #cursor visibility
    row = 0
    flag1 = True
    
    print_menu(stdscr, row, menu)
    
    while flag1:
        key = stdscr.getch()
        if key == curses.KEY_UP and row > 0:
            row -= 1
        elif key == curses.KEY_DOWN and row < 5:
            row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]: # 10 == '\n', 13 == '\r'    
            if row == 4:
                flag1 = False
            else:
                if row == 0:
                    l1_iterative(stdscr)
                elif row == 1:
                    l2_iterative(stdscr)
                elif row == 2:
                    l3_iterative(stdscr)
                elif row == 3:
                    l4_iterative(stdscr)
            pass
        print_menu(stdscr, row, menu)

curses.wrapper(main)