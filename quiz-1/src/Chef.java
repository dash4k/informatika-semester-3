class Chef extends Worker implements Cooks {
    Chef(String name, String tools) {
        super(name, tools);
    }

    void duty() {
        System.out.println("Chef " + this.name + " is preparing " + this.tools);
    }

    public void cook() {
        System.out.println("Chef " + this.name + " is cooking");
    }
}