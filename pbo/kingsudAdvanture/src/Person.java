import java.util.Random;

public class Person {
    public String name;
    public String weapon;
    public int hp;
    public int mana;
    public int damage;

    private static Random random = new Random();

    Person(String name, String weapon, int damage, int hp, int mana){
        this.name = name;
        this.hp = hp;
        this.mana = mana;
        this.weapon = weapon;
        this.damage = damage;
    }

    public void attack(Player mc){
        Random hit_rate = new Random();
        if (hit_rate.nextDouble() < 0.3) {
            System.out.println("\n" + mc.name + " attacked by " + this.name + " with " + this.weapon);
            System.out.println("\n" + mc.hp + " - " + this.damage + " = Current " + mc.name + " HP: " + (mc.hp -= this.damage));
        }
        else {
            System.out.println("\n" + this.name + " failed to attack " + mc.name + " with " + this.weapon);
        }
    }

    public void attack(NPC npc){
        Random hit_rate = new Random();
        if (hit_rate.nextDouble() < 0.85) {
            System.out.println("\n" + npc.name + " attacked by " + this.name + " with " + this.weapon);
            System.out.println("\n" + npc.hp + " - " + this.damage + " = Current " + npc.name + " HP: " + (npc.hp -= this.damage));
        }
        else {
            System.out.println("\n" + this.name + " failed to attack " + npc.name + " with " + this.weapon);
        }
    }

    public void heal(){
        if (this.mana > 0) {
            this.hp += 20;
            this.mana -= 20;
            System.out.println("\n" + this.name + " healed his hp with 20 mana, current HP: " + this.hp);
        }
    }
}
