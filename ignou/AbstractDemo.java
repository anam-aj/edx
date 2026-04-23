// Abstract class
abstract class Animal {
    // Abstract classes can have instance variables
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    // Abstract method (does not have a body)
    // Subclasses MUST provide an implementation for this
    public abstract void makeSound();

    // Regular (concrete) method
    // Subclasses inherit this behavior as-is
    public void sleep() {
        System.out.println(name + " is sleeping: Zzzzz...");
    }
}

// Concrete subclass 1
class Dog extends Animal {
    public Dog(String name) {
        super(name); // Call the constructor of the abstract class
    }

    // Implementing the abstract method
    @Override
    public void makeSound() {
        System.out.println(name + " says: Woof Woof!");
    }
}

// Concrete subclass 2
class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    // Implementing the abstract method
    @Override
    public void makeSound() {
        System.out.println(name + " says: Meow!");
    }
}

// Main class to run the program
public class AbstractDemo {
    public static void main(String[] args) {
        System.out.println("=== Abstract Class Demo ===\n");

        // Animal myAnimal = new Animal("Generic"); // ERROR: Cannot instantiate an abstract class

        // We can use the abstract class as a reference type
        Animal myDog = new Dog("Buddy");
        Animal myCat = new Cat("Whiskers");

        myDog.makeSound();
        myDog.sleep();

        System.out.println("--------------------");

        myCat.makeSound();
        myCat.sleep();
    }
}
