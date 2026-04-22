interface Drawable {
    void draw(); // implicitly public and abstract
}

class Rectangle implements Drawable {
    public void draw() {
        System.out.println("Drawing a rectangle");
    }
}
