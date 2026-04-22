interface Drawable {
    void draw(); // implicitly public and abstract
}

class Rectangle implements Drawable {
    public void draw() {
        System.out.println("Drawing a rectangle");
    }
}class MyThread extends Thread {
    public void run() {
        for(int i=1; i<=3; i++) {
            System.out.println(Thread.currentThread().getName() + " executing");
        }
    }
}

public class ThreadDemo {
    public static void main(String[] args) {
        MyThread t1 = new MyThread(); // Advantage: Threads run simultaneously
        MyThread t2 = new MyThread();
        t1.start();
        t2.start();
    }
}
