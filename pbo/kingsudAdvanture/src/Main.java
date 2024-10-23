import java.util.Scanner;
import java.util.InputMismatchException;
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
            try {    
                System.out.println("\n1. Sword\n2. Bow\n3. Axe\n4. Slingshot");
                System.out.print("\nEnter a number: ");
                mc_weapon_temp = scanner.nextInt();
                if (mc_weapon_temp > 0 && mc_weapon_temp < 5) {
                    break;
                }
            }
            catch (InputMismatchException e) {
                mc_weapon_temp = 1;
                scanner.next();
                break;
            }   
        }
        String mc_weapon = weapons[mc_weapon_temp - 1];
        int mc_weapon_damage = weapon_damages[mc_weapon_temp - 1];
        Player mc = new Player(mc_name, mc_weapon, mc_weapon_damage, 100, 100);
        int npc_count = chances.nextInt(3) + 1;
        NPC[] npcs = new NPC[npc_count + 2];
        for (int i = 0; i < npc_count; i++) {
            npcs[i] = new NPC();
        }
        npc_count += 2;
        for (int i = npc_count - 2; i < npc_count; i++) {
            if (chances.nextDouble() < 0.3) {
                npcs[i] = new NPC("Berserk");
            }
            else if (chances.nextDouble() < 0.6) {
                npcs[i] = new NPC("Archer");
            }
            else {
                npcs[i] = new NPC("Warrior");
            }
        }
        int i = 0;
        NPC boss = new NPC("Agus Perkutut", "Machete", 80, 100, 300, "Final Boss");
        for (NPC npc : npcs) {
            mc.mana = 100;
            i++;
            while (true) {
                clear();
                int choice;
                while (true) {
                    try {
                        clear();
                        System.out.println("Stage " + i );
                        System.out.println("Current HP: " + mc.hp + "\tEnemy's HP: " + npc.hp + "\n");
                        System.out.println("Choose what are you going to do!");
                        System.out.println("\n1. Attack\n2. Heal\n3. Do Nothing");
                        System.out.print("\nChoose: ");
                        choice = scanner.nextInt();
                        scanner.nextLine();
                        if (choice > 0 && choice < 4) {
                            break;
                        }
                    }
                    catch (InputMismatchException e) {
                        choice = 1;
                        scanner.next();
                        break;
                    }
                }
                if (choice == 1) {
                    while (true) {
                        try {        
                            clear();
                            System.out.println("Choose an item from your inventory\n\n");
                            for (int j = 0; j < mc.weapon.size(); j++) {
                                System.out.println((j + 1) + ". Name: " + mc.weapon.get(j) + ", Damage: " + mc.damage.get(mc.weapon.get(j)));
                            }
                            System.out.print("\n\nChoice: ");
                            choice = scanner.nextInt();
                            if (choice > 0 && choice <= mc.weapon.size()) {
                                mc.attack(npc, mc.weapon.get(choice - 1), mc.damage.get(mc.weapon.get(choice - 1)));
                                scanner.nextLine();
                                break;
                            }
                        }
                        catch (InputMismatchException e) {
                            choice = 1;
                            mc.attack(npc, mc.weapon.get(choice - 1), mc.damage.get(mc.weapon.get(choice - 1)));
                            scanner.nextLine();
                            break;
                        }
                    }
                }
                else if (choice == 2) {
                    mc.heal();
                }
                if (chances.nextDouble() > 0.5) {
                    npc.attack(mc);
                }
                else {
                    npc.heal();
                }
                if (mc.hp <= 0) {
                    System.out.println("\n" + mc.name + " has died.");
                    System.out.print("\n\nThanks for playing :D");
                    scanner.nextLine();
                    return;
                }
                else if (npc.hp <= 0) {
                    System.out.println("\n" + npc.name + " has died.");
                    if (!mc.weapon.contains(npc.weapon)) {
                        try {    
                            System.out.print("\nTake " + npc.name + "'s weapon? Name: " + npc.weapon + ", Damage: " + npc.damage);
                            System.out.println("\n1. Yes\t\t 2. No");
                            System.out.print("\nChoice: ");
                            choice = scanner.nextInt();
                            if (choice == 1) {
                                mc.get_weapon(npc.weapon, npc.damage);
                            }
                            scanner.nextLine();
                        }
                        catch (InputMismatchException e) {
                            mc.get_weapon(npc.weapon, npc.damage);
                            scanner.next();
                            break;
                        }
                    }
                    System.out.print("\nPress enter to continue...");
                    scanner.nextLine();
                    break;
                }
                System.out.print("\n\nPress enter to continue......");
                scanner.nextLine();
            }
        }
        while (true) {
            clear();
            int choice;
            while (true) {
                try {    
                    clear();
                    System.out.println("Boss Stage");
                    System.out.println("Current HP: " + mc.hp + "\tEnemy's HP: " + boss.hp + "\n");
                    System.out.println("Choose what are you going to do!");
                    System.out.println("\n1. Attack\n2. Heal\n3. Do Nothing");
                    System.out.print("\nChoose: ");
                    choice = scanner.nextInt();
                    scanner.nextLine();
                    if (choice > 0 && choice < 4) {
                        break;
                    }
                }
                catch (InputMismatchException e) {
                    choice = 1;
                    scanner.next();
                    break;
                }
            }
            if (choice == 1) {
                while (true) {
                    try {    
                        clear();
                        System.out.println("Choose an item from your inventory\n\n");
                        for (int j = 0; j < mc.weapon.size(); j++) {
                            System.out.println((j + 1) + ". Name: " + mc.weapon.get(j) + ", Damage: " + mc.damage.get(mc.weapon.get(j)));
                        }
                        System.out.print("\n\nChoice: ");
                        choice = scanner.nextInt();
                        if (choice > 0 && choice <= mc.weapon.size()) {
                            mc.attack(boss, mc.weapon.get(choice - 1), mc.damage.get(mc.weapon.get(choice - 1)));
                            scanner.nextLine();
                            break;
                        }
                    }
                    catch (InputMismatchException e) {
                        choice = 1;
                        mc.attack(boss, mc.weapon.get(choice - 1), mc.damage.get(mc.weapon.get(choice - 1)));
                        scanner.nextLine();
                        break;
                    }
                }
            }
            else if (choice == 2) {
                mc.heal();
            }
            if (chances.nextDouble() > 0.5) {
                boss.attack(mc);
            }
            else {
                boss.heal();
            }
            if (mc.hp <= 0) {
                System.out.println("\n" + mc.name + " has died.");
                System.out.print("\n\nThanks for playing :D");
                scanner.nextLine();
                break;
            }
            else if (boss.hp <= 0) {
                System.out.println("\n" + boss.name + " has died.");
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