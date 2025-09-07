from util import print_menu, lang
import curses

def main(stdscr):
    menu = [
        "L1 (Starts with '10' & ends with '01')", 
        "L2 (Contains '000' & ends with '1')", 
        "L3 (Starts & ends with different symbol)", 
        "L4 (Starts & ends with identical symbol & contains '101')", 
        "Exit"
        ]
    curses.curs_set(0) #cursor visibility
    row = 0
    flag1 = True
    
    print_menu(stdscr, row, menu)
    
    while flag1:
        key = stdscr.getch()
        if key == curses.KEY_UP and row > 0:
            row -= 1
        elif key == curses.KEY_DOWN and row < 4:
            row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]: # 10 == '\n', 13 == '\r'    
            if row == 4:
                flag1 = False
            else:
                if row == 0:
                    lang(stdscr, 1)
                elif row == 1:
                    lang(stdscr, 2)
                elif row == 2:
                    lang(stdscr, 3)
                elif row == 3:
                    lang(stdscr, 4)
            pass
        print_menu(stdscr, row, menu)

curses.wrapper(main)