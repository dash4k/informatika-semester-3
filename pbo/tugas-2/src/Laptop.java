import java.util.Random;

public class Laptop {
    double cpu_health;
    double gpu_health;
    double mem_health;
    String cpu;
    String gpu;
    String mem;

    private static Random random = new Random();

    Laptop(String cpu, String gpu, String mem) {
        this.cpu = cpu;
        this.gpu = gpu;
        this.mem = mem;
    }

    void checkHealth() {
        cpu_health = random.nextDouble() * 100;
        gpu_health = random.nextDouble() * 100;
        mem_health = random.nextDouble() * 100;
    }

    boolean fixBrokenCPU() {
        if (random.nextInt(100) > 30) {
            cpu_health = 100.00;
            return true;
        }
        else {
            return false;
        }
    }

    boolean fixBrokenGPU() {
        if (random.nextInt(100) > 30) {
            gpu_health = 100.00;
            return true;
        }
        else {
            return false;
        }
    }

    boolean fixBrokenMEM() {
        if (random.nextInt(100) > 30) {
            mem_health = 100.00;
            return true;
        }
        else {
            return false;
        }
    }
}