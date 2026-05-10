

class Rough3 {

    static int add(int a, int b) {

        return a + b;

    }



    public static void main(String[] args) {

        System.out.println(add(10,20));

    }

}




Question 2

Write a Java
program to find factorial using method.


class MethodFactorial {

    static int fact(int n) {

        int f = 1;



        for(int i=1;i<=n;i++)

            f *= i;



        return f;

    }



    public static void main(String[] args) {

        System.out.println(fact(5));

    }

}




Question 3

Write a Java
program to find square using method.


class SquareMethod {

    static int square(int n) {

        return n * n;

    }



    public static void main(String[] args) {

        System.out.println(square(6));

    }

}




Question 4

Write a Java
program demonstrating method overloading.


class Overloading {

    void add(int a, int b) {

        System.out.println(a +
b);

    }



    void add(int a, int b, int c) {

        System.out.println(a +
b + c);

    }



    public static void main(String[] args) {

        Overloading
obj = new Overloading();

        obj.add(10,20);

        obj.add(10,20,30);

    }

}
*/
