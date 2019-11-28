import java.util.ArrayList;
import java.util.Arrays;

class Rand_b_X {
public void rand(){
        int N[] = {10, 1000, 1000000};
        System.out.println("RAND1");
        for(int i=0; i<N.length; i++) {
                System.out.println("n = " + N[i]);
                int rand1[] = this.RAND1(N[i]);
                double per_rand1[] = this.histogram(rand1);
                System.out.println(Arrays.toString(per_rand1));
        }
        System.out.println("\n");


        System.out.println("RAND2");
        for(int i=0; i<N.length; i++) {
                System.out.println("n = " + N[i]);
                int rand2[] = this.RAND2(N[i]);
                double per_rand2[] = this.histogram(rand2);
                System.out.println(Arrays.toString(per_rand2));
        }
        System.out.println("\n");

        System.out.println("RAND3");
        for(int i=0; i<N.length; i++) {
                System.out.println("n = " + N[i]);
                int rand3[] = this.RAND3(N[i]);
                double per_rand3[] = this.histogram(rand3);
                double sum = 0;
                for(int j=0; j<per_rand3.length; j++) {
                        per_rand3[j] = ((per_rand3[j]-10)*(per_rand3[j]-10))/10;
                        sum += per_rand3[j];
                }
                System.out.println("Observd: " + Arrays.toString(per_rand3));
                System.out.println("D = " + sum);
        }
        System.out.println("\n");
}

public int[] RAND1(int n){
        int x = 53402397;
        int A = 65539;
        int M = 2147483647;
        int C = 125654;
        int rand_seq[] = new int[n];
        for(int i=0; i<n; i++) {
                x = A * x + C;
                if(x < 0) {
                        x += M;
                        x += 1;
                }
                rand_seq[i] = x;
        }
        return rand_seq;
}

public int[] RAND2(int n){
        int x = 1;
        int A = 48271;
        int M = 2147483647;
        double Q = M / A;
        double R = M % A;
        int rand_seq[] = new int[n];
        for(int i=0; i<n; i++) {
                x = (int)(A * (x % Q) - R * (x / Q));
                if(x < 0) {
                        x += M;
                }
                rand_seq[i] = x;
        }
        return rand_seq;
}

public int[] RAND3(int n){
        int x = 1;
        int next = 0;
        int A[] = this.RAND2(55);
        int M = 2147483647;
        int rand_seq[] = new int[n];
        for(int i=0; i<n; i++) {
                int j = (next + 31) % 55;
                x = A[j] - A[next];
                if(x < 0) {
                        x += M;
                        x += 1;
                }
                A[next] = x;
                next = (next + 1) % 55;
                rand_seq[i] = x;
        }
        return rand_seq;
}

public double[] histogram(int R[]){
        double M = 2147483647;
        double per[] = new double[10];
        int n = R.length;;
        for(int i=0; i<n; i++) {
                double num = R[i]/M;
                if (num >= 0 && num < 0.1) per[0] += 1;
                else if (num >= 0.1 && num < 0.2) per[1] += 1;
                else if (num >= 0.2 && num < 0.3) per[2] += 1;
                else if (num >= 0.3 && num < 0.4) per[3] += 1;
                else if (num >= 0.4 && num < 0.5) per[4] += 1;
                else if (num >= 0.5 && num < 0.6) per[5] += 1;
                else if (num >= 0.6 && num < 0.7) per[6] += 1;
                else if (num >= 0.7 && num < 0.8) per[7] += 1;
                else if (num >= 0.8 && num < 0.9) per[8] += 1;
                else if (num >= 0.9 && num < 1.0) per[9] += 1;
        }
        for(int i=0; i<10; i++) {
                per[i] = per[i] / n * 100;
                // 3 digits after the decimal point
                per[i] = (int)(per[i]*1000);
                per[i] /= 1000;
        }
        return per;
}

public static void main(String[] args){
        Rand_b_X b = new Rand_b_X();
        b.rand();
}
}
