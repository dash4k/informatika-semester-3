import java.util.ArrayList;
import java.util.HashMap;

public class Player extends Person {
    public ArrayList<String> weapon = new ArrayList<>();
    public HashMap<String, Integer> damage = new HashMap<>();

    Player(String name, String weapon, int damage, int hp, int mana){
        super(name, "", 0, hp, mana);
        this.weapon.add(weapon);
        this.damage.put(weapon, damage);
    }

    public void get_weapon(String name, int damage){
        System.out.println("\n" + this.name + " grabbed " + name);
        this.weapon.add(name);
        this.damage.put(name, damage);
    }
}
