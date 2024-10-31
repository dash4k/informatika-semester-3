from stringMatching import match
from shortestPath import *
from util import *

flag = True
while flag:
    clear()
    print("╔════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                  Choose an Algorithm                                   ║")
    print("║                                                                                        ║")
    print("║                                  [1]   String Matching                                 ║")
    print("║                                  [2]   Shortest Path                                   ║")
    print("║                                  [3]   Exit                                            ║")
    print("║                                                                                        ║")
    print("╚════════════════════════════════════════════════════════════════════════════════════════╝")
    x = ask_int("Choice: ")
    if x == 1:
        clear()
        print("Input a long string")
        ls = input("Input: ")
        print("\nInput another string to match the previous string")
        ss = input("Input: ")
        result = match(ls, ss, len(ls), len(ss))
        if result != -1:
            print(f"{ss} found at index {result} - {result + len(ss)}")
        else:
            print(f"{ss} not found in {ls}")
        input("\n\nPress enter to continue........")
    elif x == 2:
        clear()
        points = []
        for i in range(4):
            clear()
            for point in points:
                print(point)
            temp1 = ask_int("Enter x:")
            temp2 = ask_int("Enter y: ")
            temp3 = Dots(temp1, temp2)
            points.append(temp3)
        p1, p2 = sp(points, 4)
        clear()
        print(f"Shortest path is between {p1} and {p2}")
        input("\n\nPress enter to continue........")
    elif x == 3:
        flag = False
    else:
        continue