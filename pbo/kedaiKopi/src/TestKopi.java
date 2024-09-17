public class TestKopi {
    public static void main(String[] args) {
        // Create an instance of Kopi (the order system)
        Kopi order_list = new Kopi();

        // Adding items to the order
        System.out.println("Adding items to the order:");
        order_list.add(1);  // Add Espresso
        order_list.add(2);  // Add Cappuccino
        order_list.add(3);  // Add Latte
        order_list.add(1);  // Add another Espresso
        order_list.add(5);  // Add Macchiato

        // Print the current table with orders
        System.out.println("\nCurrent Orders:");
        order_list.printTable();

        // Delete an item from the list (decrease quantity or remove if quantity <= 0)
        System.out.println("\nRemoving one Espresso:");
        order_list.delete(1);

        // Print the updated order list
        System.out.println("\nUpdated Orders:");
        order_list.printTable();

        // Try removing an item not in the list
        System.out.println("\nTrying to remove an item not in the list (Americano):");
        order_list.delete(4); // Deleting an item that wasn't added yet

        // Print the order list again
        System.out.println("\nFinal Orders:");
        order_list.printTable();
    }
}
