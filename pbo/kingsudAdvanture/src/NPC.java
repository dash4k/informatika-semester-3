public class NPC extends Person {
    private String job;

    NPC(String name, String weapon, int damage, int hp, int mana, String job){
        super(name, weapon, damage, hp, mana);
        this.job = job;
    }
}
