class Animal { // Grandparent
    void eat() { System.out.println("Eating..."); }
}
class Dog extends Animal { // Parent
    void bark() { System.out.println("Barking..."); }
}
class Puppy extends Dog { // Child
    void weep() { System.out.println("Weeping..."); }
}

public class MultilevelDemo {
    public static void main(String[] args) {
        Puppy p = new Puppy();
        p.eat();  // Inherited from Animal
        p.bark(); // Inherited from Dog
        p.weep(); // Own method
    }
}
