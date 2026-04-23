public class OperatorDemonstration {

    public static void main(String[] args) {

        System.out.println("=== Java Operators Demonstration ===\n");

        // 1. Arithmetic Operators
        System.out.println("--- 1. Arithmetic Operators ---");
        int a = 10;
        int b = 5;
        System.out.println("Variables: a = " + a + ", b = " + b);
        System.out.println("Addition (a + b): " + (a + b));
        System.out.println("Subtraction (a - b): " + (a - b));
        System.out.println("Multiplication (a * b): " + (a * b));
        System.out.println("Division (a / b): " + (a / b));
        System.out.println("Modulo (a % b): " + (a % b)); // Returns the remainder

        // 2. Unary Operators
        System.out.println("\n--- 2. Unary Operators ---");
        int c = 10;
        boolean flag = true;
        System.out.println("Variables: c = " + c + ", flag = " + flag);
        System.out.println("Post-increment (c++): " + (c++)); // Prints 10, then increments to 11
        System.out.println("Pre-increment (++c): " + (++c));  // Increments to 12, then prints 12
        System.out.println("Pre-decrement (--c): " + (--c));  // Decrements to 11, then prints 11
        System.out.println("Logical Invert (!flag): " + (!flag));

        // 3. Relational (Comparison) Operators
        System.out.println("\n--- 3. Relational Operators ---");
        System.out.println("Variables: a = " + a + ", b = " + b);
        System.out.println("Equal to (a == b): " + (a == b));
        System.out.println("Not equal to (a != b): " + (a != b));
        System.out.println("Greater than (a > b): " + (a > b));
        System.out.println("Less than or equal to (a <= b): " + (a <= b));

        // 4. Logical Operators
        System.out.println("\n--- 4. Logical Operators ---");
        boolean x = true;
        boolean y = false;
        System.out.println("Variables: x = " + x + ", y = " + y);
        System.out.println("Logical AND (x && y): " + (x && y)); // True if both are true
        System.out.println("Logical OR (x || y): " + (x || y));  // True if at least one is true
        System.out.println("Logical NOT (!x): " + (!x));         // Reverses the boolean state

        // 5. Assignment Operators
        System.out.println("\n--- 5. Assignment Operators ---");
        int num = 20;
        System.out.println("Initial value: num = " + num);

        num += 10; // Equivalent to: num = num + 10
        System.out.println("Add and assign (num += 10): " + num);

        num *= 2;  // Equivalent to: num = num * 2
        System.out.println("Multiply and assign (num *= 2): " + num);

        num /= 5;  // Equivalent to: num = num / 5
        System.out.println("Divide and assign (num /= 5): " + num);
    }
}
