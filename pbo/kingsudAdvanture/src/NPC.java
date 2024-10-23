public class NPC extends Person {
    private static int id = 0;
    private String job;

    NPC(String name, String weapon, int damage, int hp, int mana, String job){
        super(name, weapon, damage, hp, mana);
        this.job = job;
    }

    NPC(String job){
        this();
        this.job = job;
        if (job == "Warrior") {
            super.name = "Unnamed Warrior";
            super.weapon = "Sword";
            super.damage = 30;
            super.hp = 100;
            super.mana = 100;
        }
        else if (job == "Archer") {
            super.name = "Unnamed Archer";
            super.weapon = "Bow";
            super.damage = 20;
            super.hp = 100;
            super.mana = 200;
        }
        else if (job == "Berserk") {
            super.name = "Unnamed Berserk";
            super.weapon = "Axe";
            super.damage = 40;
            super.hp = 200;
            super.mana = 10;
        }
    }

    NPC(){
        super(("Clown_" + id++), "Stick", 10, 75, 35);
        this.job = "Clown";
    }
}
