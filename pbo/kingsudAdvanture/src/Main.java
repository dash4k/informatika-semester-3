import java.util.Scanner;
import java.util.Random;

public class Main {
    private static Random chances = new Random();
    public static void main(String[] args) {
        clear();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String mc_name = scanner.nextLine();
        System.out.println("\nSelect your weapon:");
        String[] weapons = {"Sword", "Bow", "Axe", "Slingshot"};
        int[] weapon_damages = {30, 20, 40, 100};
        int mc_weapon_temp;
        while (true) {
            System.out.println("\n1. Sword\n2. Bow\n3. Axe\n4. Slingshot");
            System.out.print("\nEnter a number: ");
            mc_weapon_temp = scanner.nextInt();
            if (mc_weapon_temp > 0 & mc_weapon_temp < 5) {
                break;
            }   
        }
        String mc_weapon = weapons[mc_weapon_temp - 1];
        int mc_weapon_damage = weapon_damages[mc_weapon_temp - 1];
        Player mc = new Player(mc_name, mc_weapon, mc_weapon_damage, 100, 100);
        NPC npc1 = new NPC("Agus Perkutut", "Sword", 30, 100, 100, "Juragan Perkutut");
        while (true) {
            clear();
            int choice;
            while (true) {
                clear();
                System.out.println("Choose what are you going to do!");
                System.out.println("\n1. Attack\n2. Heal\n3. Do Nothing");
                System.out.print("\nChoose: ");
                choice = scanner.nextInt();
                scanner.nextLine();
                if (choice > 0 & choice < 4) {
                    break;
                }
            }
            if (chances.nextDouble() > 0.5) {
                npc1.attack(mc);
            }
            else {
                npc1.heal();
            }
            if (choice == 1) {
                mc.attack(npc1);
            }
            else if (choice == 2) {
                mc.heal();
            }
            if (mc.hp <= 0) {
                System.out.println("\n" + mc.name + " has died.");
                System.out.print("\n\nThanks for playing :D");
                scanner.nextLine();
                break;
            }
            else if (npc1.hp <= 0) {
                System.out.println("\n" + npc1.name + " has died.");
                System.out.print("\n\nThanks for playing :D");
                scanner.nextLine();
                break;
            }
            System.out.print("\n\nPress enter to continue......");
            scanner.nextLine();
        }
        scanner.close();
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