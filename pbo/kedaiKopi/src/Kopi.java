public class Kopi {
    
    // Node class representing the user's order
    private class Node {

        // Order's attributes
        int id, qty, price;
        String name;
        Node next;
        Node prev;

        // Node's constructor
        Node(int id, String name, int price) {
            this.id = id;
            this.name = name;
            this.price = price;
            this.qty = 1;
            this.next = null;
            this.prev = null;
        }
    }

    // Node head & tail pointer
    private Node head;
    private Node tail;
    
    // Total Price
    public int total;

    // Method for adding new item to the list
    public boolean add(int id) {
        Node new_node = null;
        
        switch (id) {
            case 1:
                new_node = new Node(id, "Espresso", 15000);
                break;

            case 2:
                new_node = new Node(id, "Cappuccino", 25000);
                break;

            case 3:
                new_node = new Node(id, "Latte", 24500);
                break;
            case 4:
                new_node = new Node(id, "Americano", 21000);
                break;

            case 5:
                new_node = new Node(id, "Macchiato", 22500);
                break;

            default:
                return false;
        }

        // If the list is empty
        if (head == null) {
            head = new_node;
            tail = new_node;
            return true;
        }
        else {
            // Check whether the order is already inside the list
            Node curr = head;
            while (curr != null) {
                if (curr.id == id) {
                    curr.qty++;
                    curr.price = new_node.price * curr.qty;
                    return true;
                }
                curr = curr.next;
            }
            // Add new node to the list if there's no similar node inside the list
            tail.next = new_node;
            new_node.prev = tail;
            tail = new_node;
            return true;
        }
    }

    // Helper method for removing a node (order) from a list
    private boolean remove_node(Node curr) {
        if (curr == null) {
            return false;
        }
        // If it's the only order inside the list
        else if (curr == head && curr == tail) {
            head = null;
            tail = null;
        }
        // If the order is the same as head pointer
        else if (curr == head) {
            head = head.next;
            // Check whether the head is pointing to other node
            if (head != null) {
                head.prev = null;   
            }
            // If head turns out to be null, set tail to be null also
            else {
                tail = null;
            }
        }
        // If the order is the same as tail pointer
        else if (curr == tail) {
            tail = tail.prev;
            // Check whether the tail is pointing to other node
            if (tail != null) {
                tail.next = null;
            }
            // If tail turns out to be null, set head to be null also
            else {
                head = null;
            }
        }
        // If the order is in the middle of the list
        else {
            curr.prev.next = curr.next;
            curr.next.prev = curr.prev;
        }
        return true;
    }

    // Method for deleting or decreasing an order from a list 
    public boolean delete(int id) {
        if (head == null) {
            return false;
        }
        else {
            // Check whether the inputted id is in the list
            Node curr = head;
            while (curr != null) {
                if (curr.id == id) {
                    curr.qty--;
                    // If the current quantity of the id is less than or equal to zero, remove the node from the list
                    if (curr.qty <= 0) {
                        return remove_node(curr);
                    }
                    return true;
                }
                curr = curr.next;
            }
            return false;
        }
    }

    // Method for printing the order
    public boolean printTable() {
        total = 0;
        if (head == null) {
            return false;
        }
        // Print header
        System.out.format("%-5s %-10s %-5s %-10s%n%n", "ID", "Name", "Qty", "Price");

        // Traverse the node and print the order
        Node curr = head;
        while (curr != null) {
            System.out.format("%-5d %-10s %-5d %-10d%n", curr.id, curr.name, curr.qty, curr.price);
            total += curr.price;
            curr = curr.next;
        }

        // Print total
        System.out.format("%n%-13s %14d%n%n", "Total", total);
        return true;
    }
}