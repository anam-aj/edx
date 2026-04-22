public class InterestCalculator {
    public double calculateSimpleInterest(double p, double r, double t) {
        return (p * r * t) / 100;
    }

    public double calculateCompoundInterest(double p, double r, double t) {
        return p * Math.pow((1 + r / 100), t) - p;
    }

    public static void main(String[] args) {
        InterestCalculator calc = new InterestCalculator();
        double principal = 10000;
        double rate = 5.5;
        double time = 3;

        System.out.println("Simple Interest: " + calc.calculateSimpleInterest(principal, rate, time));
        System.out.println("Compound Interest: " + calc.calculateCompoundInterest(principal, rate, time));
    }
}
