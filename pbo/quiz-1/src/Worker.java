abstract class Worker {
    public String name;
    public String tools;

    Worker(String name, String tools) {
        this.name = name;
        this.tools = tools;
    }

    abstract void duty();
    
    void rest() {
        System.out.println(this.name + " is resting");
    }
}