import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        boolean flag1 = true;
        int amount = 0;

        System.out.print("CPU: ");
        String cpu = scanner.nextLine();
        System.out.print("GPU: ");
        String gpu = scanner.nextLine();
        System.out.print("MEMORY: ");
        String mem = scanner.nextLine();

        Laptop laptop = new Laptop(cpu, gpu, mem);

        while (flag1) { 
            System.out.println("1. Check Laptop's Health");    
            System.out.println("2. Fix Laptop's Health");    
            System.out.println("3. Payment");    
            System.out.println("4. Exit");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    laptop.checkHealth();
                    System.out.print("CPU Health: ");
                    System.out.println(laptop.cpu_health);
                    System.out.print("GPU Health: ");
                    System.out.println(laptop.gpu_health);
                    System.out.print("MEMORY Health: ");
                    System.out.println(laptop.mem_health);
                    scanner.nextLine(); 
                    System.out.print("Press Enter to go back..... ");
                    scanner.nextLine();
                    break;
                
                case 2:
                    if (laptop.cpu_health < 50) {
                        if (laptop.fixBrokenCPU()) {
                            amount++;
                            System.out.println("CPU Successfully Recovered!");
                        }
                    }
                    
                    if (laptop.gpu_health < 50) {
                        if (laptop.fixBrokenGPU()) {
                            amount++;
                            System.out.println("GPU Successfully Recovered!");
                        }
                    }
                    
                    if (laptop.mem_health < 50) {
                        if (laptop.fixBrokenMEM()) {
                            amount++;
                            System.out.println("Memory Successfully Recovered!");
                        }
                    }
                    scanner.nextLine(); 
                    System.out.print("Press Enter to go back..... ");
                    scanner.nextLine();
                    break;
                
                case 3:
                    Shop new_bill = new Shop(amount);
                    new_bill.addBill();

                    System.out.println("Bill: "+new_bill.bill);
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
}