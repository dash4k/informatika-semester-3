public class Shop {
    int services;
    int bill;
    int payment;

    Shop(int services) {
        this.services = services;
    }

    int addBill() {
        bill = services * 1000;
        return bill;
    }

    boolean proceedPayment(int payment) {
        this.payment = payment;
        if (bill <= this.payment) {
            return true;
        }
        else {
            return false;
        }
    }
}
