abstract class Shape {
    // Abstract method (no body)
    abstract void draw();
}

class Circle extends Shape {
    // Providing implementation
    void draw() {
        System.out.println("Drawing a circle");
    }
}
