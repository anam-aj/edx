import java.io.*;

public class FileStreamExample {
    public static void main(String[] args) {
        try {
            // OutputStream: Writing bytes
            FileOutputStream out = new FileOutputStream("test.txt");
            out.write(65); // Writes the ASCII character 'A'
            out.close();

            // InputStream: Reading bytes
            FileInputStream in = new FileInputStream("test.txt");
            int data = in.read();
            System.out.println("Read from file: " + (char)data);
            in.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
