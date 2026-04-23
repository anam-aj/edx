class SharedBuffer {
    private int item;
    private boolean hasItem = false;

    // Synchronized method for Producer
    public synchronized void produce(int item) {
        while (hasItem) {
            try {
                wait(); // Wait if the buffer is full
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        this.item = item;
        System.out.println("Produced: " + item);
        hasItem = true;
        notify(); // Notify the waiting Consumer
    }

    // Synchronized method for Consumer
    public synchronized void consume() {
        while (!hasItem) {
            try {
                wait(); // Wait if the buffer is empty
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        System.out.println("Consumed: " + item);
        hasItem = false;
        notify(); // Notify the waiting Producer
    }
}

class Producer extends Thread {
    private SharedBuffer buffer;

    public Producer(SharedBuffer buffer) {
        this.buffer = buffer;
    }

    public void run() {
        for (int i = 1; i <= 5; i++) {
            buffer.produce(i);
        }
    }
}

class Consumer extends Thread {
    private SharedBuffer buffer;

    public Consumer(SharedBuffer buffer) {
        this.buffer = buffer;
    }

    public void run() {
        for (int i = 1; i <= 5; i++) {
            buffer.consume();
        }
    }
}

public class ThreadDemo {
    public static void main(String[] args) {
        SharedBuffer buffer = new SharedBuffer();

        Producer producerThread = new Producer(buffer);
        Consumer consumerThread = new Consumer(buffer);

        // Demonstrating Thread Priorities
        producerThread.setPriority(Thread.MIN_PRIORITY); // Priority 1
        consumerThread.setPriority(Thread.MAX_PRIORITY); // Priority 10

        System.out.println("Producer Priority: " + producerThread.getPriority());
        System.out.println("Consumer Priority: " + consumerThread.getPriority());
        System.out.println("Starting threads...\n");

        producerThread.start();
        consumerThread.start();
    }
}
