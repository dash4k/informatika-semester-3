import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        boolean flag1 = true;
        int amount = 0;

        clear();
        System.out.print("CPU: ");
        String cpu = scanner.nextLine();
        System.out.print("GPU: ");
        String gpu = scanner.nextLine();
        System.out.print("MEMORY: ");
        String mem = scanner.nextLine();

        Laptop laptop = new Laptop(cpu, gpu, mem);

        while (flag1) {
            clear(); 
            System.out.println("1. Check Laptop's Health");    
            System.out.println("2. Fix Laptop's Health");    
            System.out.println("3. Payment");    
            System.out.println("4. Exit");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    clear();
                    laptop.checkHealth();
                    System.out.print("CPU Health: ");
                    System.out.println(String.format("%.2f%%", laptop.cpu_health));
                    System.out.print("GPU Health: ");
                    System.out.println(String.format("%.2f%%", laptop.gpu_health));
                    System.out.print("MEMORY Health: ");
                    System.out.println(String.format("%.2f%%", laptop.mem_health));
                    scanner.nextLine(); 
                    System.out.print("Press Enter to go back..... ");
                    scanner.nextLine();
                    break;
                
                case 2:
                    clear();
                    if (laptop.cpu_health < 50) {
                        if (laptop.fixBrokenCPU()) {
                            amount++;
                            System.out.println("CPU Successfully Recovered!");
                        }
                    }
                    else {
                        System.out.println("CPU Not Successfully Recovered!");
                    }
                    
                    if (laptop.gpu_health < 50) {
                        if (laptop.fixBrokenGPU()) {
                            amount++;
                            System.out.println("GPU Successfully Recovered!");
                        }
                    }
                    else {
                        System.out.println("GPU Not Successfully Recovered!");
                    }
                    
                    if (laptop.mem_health < 50) {
                        if (laptop.fixBrokenMEM()) {
                            amount++;
                            System.out.println("Memory Successfully Recovered!");
                        }
                    }
                    else {
                        System.out.println("Memory Not Successfully Recovered!");
                    }
                    scanner.nextLine(); 
                    System.out.print("Press Enter to go back..... ");
                    scanner.nextLine();
                    break;
                
                case 3:
                    clear();
                    Shop new_bill = new Shop(amount);
                    int bill = new_bill.addBill();
                    System.out.println("Bill: "+bill);
                    System.out.print("Payment: ");
                    int pay = scanner.nextInt();
                    
                    if (new_bill.proceedPayment(pay)) {
                        System.out.println("Success!");
                    }
                    else {
                        System.out.println("Failed!");
                    }
                    scanner.nextLine(); 
                    System.out.print("Press Enter to go back..... ");
                    scanner.nextLine();
                    break;

                case 4:
                    flag1 = false;
                    break;
                default:
                    break;
            }
        }
    }    

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