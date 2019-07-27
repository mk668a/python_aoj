import java.util.Random;
import java.util.Arrays;

class Randomized {

public double PI(int n){
        double inCircle = 0;
        Random rand = new Random();
        for (int i = 0; i<n; i++) {
                double x = rand.nextDouble();
                double y = rand.nextDouble();
                double d = (x - 0.5)*(x - 0.5) + (y - 0.5)*(y - 0.5);
                if (d < 0.25) {
                        inCircle = inCircle + 1;
                }
        }
        return 4 * inCircle / n;
}

public static void main(String[] args){
        Randomized rnd = new Randomized();
        int n = 1;
        for (int i = 1; i<7; i++) {
                System.out.println("N ="+n);
                double list[] = new double[10];
                for (int k = 0; k<10; k++) {
                        list[k] = rnd.PI(n);
                }
                System.out.println(Arrays.toString(list));
                n *= 10;
        }
}
}
