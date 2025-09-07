import java.util.InputMismatchException;
import java.util.Scanner;


public class Main {

    // Scanner for user input
    private static final Scanner scanner = new Scanner(System.in);
    
    public static void main(String[] args) {
        // Variable declaration
        Kopi order_list = new Kopi();
        boolean flag1 = true, flag2 = true;
        IntWrapper choice1 = new IntWrapper(0), choice2 = new IntWrapper(0), choice4 = new IntWrapper(0), cash = new IntWrapper(0);
        CharWrapper choice3 = new CharWrapper(null);
        
        // Menu Loop
        while (flag1) {
            // Main Menu
            clear();
            System.out.println("Main Menu\n");
            System.out.println("1. Order");
            System.out.println("2. View");
            System.out.println("3. Exit");
            System.out.print("\nChoice: ");
            if (ask_int(choice1)) {
                switch (choice1.value) {
                    // Order from menu
                    case 1:
                        clear();
                        System.out.format("%-5s %-10s %-5s%n%n", "ID", "Name", "Price");
                        System.out.format("%-5d %-10s %10d%n", 1, "Espresso", 15000);
                        System.out.format("%-5d %-10s %10d%n", 2, "Cappuccino", 25000);
                        System.out.format("%-5d %-10s %10d%n", 3, "Latte", 24500);
                        System.out.format("%-5d %-10s %10d%n", 4, "Americano", 21000);
                        System.out.format("%-5d %-10s %10d%n", 5, "Macchiato", 22500);
                        System.out.print("\nChoice: ");
                        if (ask_int(choice2)) {
                            // If order is correct
                            if (order_list.add(choice2.value)) {
                                System.out.println("Success");
                                System.out.print("Press Enter to go back..... ");
                                scanner.nextLine();
                            }
                            // If order is incorrect
                            else {
                                System.err.println("Failed");
                                System.out.print("Press Enter to go back..... ");
                                scanner.nextLine();
                            }
                        }
                        break;
                    // Edit current order
                    case 2:
                        flag2 = true;
                        while (flag2) {
                            clear();
                            if (order_list.printTable()) {
                                System.out.println("A. Increase     B. Decrease\nC. Checkout     D. Back\n");
                                System.out.print("Choice: ");
                                if (ask_char(choice3)) {
                                    switch (choice3.value.toLowerCase()) {
                                        // Add to the current order
                                        case "a":
                                            clear();
                                            if (order_list.printTable()) {
                                                System.out.print("Choice: ");
                                                if (ask_int(choice4)) {
                                                    if (order_list.search(choice4.value)) {
                                                        order_list.add(choice4.value);
                                                        System.out.println("Success");
                                                        System.out.print("Press Enter to go back..... ");
                                                        scanner.nextLine();   
                                                    }
                                                    else {
                                                        System.err.println("Failed");
                                                        System.out.print("Press Enter to go back..... ");
                                                        scanner.nextLine();
                                                    }
                                                }
                                            }
                                            break;
                                        // Subtract from the current order
                                        case "b":
                                            clear();
                                            if (order_list.printTable()) {
                                                System.out.print("Choice: ");
                                                if (ask_int(choice4)) {
                                                    if (order_list.delete(choice4.value)) {
                                                        System.out.println("Success");
                                                        System.out.print("Press Enter to go back..... ");
                                                        scanner.nextLine();   
                                                    }
                                                    else{
                                                        System.err.println("Failed");
                                                        System.out.print("Press Enter to go back..... ");
                                                        scanner.nextLine();
                                                    }
                                                }
                                            }
                                            break;
                                        // Checkout the order (reset the order)
                                        case "c":
                                            System.out.print("Cash: ");
                                            if (ask_int(cash)) {
                                                if (cash.value > order_list.total) {
                                                    order_list = new Kopi();
                                                    System.out.println("Success");
                                                    System.out.print("Press Enter to go back..... ");
                                                    scanner.nextLine();
                                                }
                                                else {
                                                    System.err.println("Failed");
                                                    System.out.print("Press Enter to go back..... ");
                                                    scanner.nextLine();
                                                }
                                            }
                                            break;
                                        // Back to the Main Menu
                                        case "d":
                                            flag2 = false;
                                            break;
                                        default:
                                            break;
                                    }
                                }
                            }
                            // Back to the Main Menu
                            else {
                                flag2 = false;
                            }   
                        }
                        break;
                    // Exit the program
                    case 3:
                        flag1 = false;
                        break;
                    default:
                        break;
                }
            }
        }
        // close the scanner
        scanner.close();
    }

    // Integer wrapper for ask_int
    public static class IntWrapper {
        public int value;
    
        public IntWrapper(int value) {
            this.value = value;
        }
    }

    // Character wrapper for ask_char
    public static class CharWrapper {
        public String value;
    
        public CharWrapper(String value) {
            this.value = value;
        }
    }

    // Function to ask the user for an integer
    public static boolean ask_int(IntWrapper x) {
        try {
            x.value = scanner.nextInt();
            scanner.nextLine();
            return true;
        } 
        catch (InputMismatchException e) {
            scanner.next();
            return false;
        }
    }

    // Function to ask the user for an char
    public static boolean ask_char(CharWrapper x) {
        try {
            String input = scanner.nextLine().trim();
            if (input.length() == 1) {
                x.value = input;
                return true;   
            }
            else {
                return false;
            }
        } 
        catch (Exception e) {
            return false;
        }
    }

    // Function to clear the terminal screen
    public static void clear() {
        try {
            if (System.getProperty("os.name").contains("Windows")) {
                // Windows
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                //Linux or Mac
                new ProcessBuilder("clear").inheritIO().start().waitFor();
            }
        }
        catch (Exception e) {
            // Handle any exceptions (IOException, InterruptedException)
            System.err.println("Error while clearing the console");
        }
    }
}
