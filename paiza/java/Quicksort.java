import java.util.Random;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Stream;

class Quicksort {
public void RandomizedSort(ArrayList<Integer> S){
        int len_S = S.size();
        if(len_S == 0) {
                return;
        }else{
                ArrayList<Integer> S_left = new ArrayList<>();
                ArrayList<Integer> S_right = new ArrayList<>();
                // choose ai ∈ S randomly
                Random rand = new Random();
                int i = rand.nextInt(len_S);
                int ai = S.get(i).intValue();
                // for each ai ∈ S:
                for(int j = 0; j<len_S; j++) {
                        int a = S.get(j).intValue();
                        if (a < ai) {
                                S_left.add(a);
                        }
                        if (a > ai) {
                                S_right.add(a);
                        }
                }
                RandomizedSort(S_left);
                // System.out.printf("%d ", ai);
                RandomizedSort(S_right);
        }
}

public void DeterministicSort(ArrayList<Integer> S){
        int len_S = S.size();
        if(len_S == 0) {
                return;
        }else{
                ArrayList<Integer> S_left = new ArrayList<>();
                ArrayList<Integer> S_right = new ArrayList<>();
                // choose median of S as ai
                int i = len_S/2;
                int ai = S.get(i).intValue();
                // for each ai ∈ S:
                for(int j = 0; j<len_S; j++) {
                        int a = S.get(j).intValue();
                        if (a < ai) {
                                S_left.add(a);
                        }
                        if (a > ai) {
                                S_right.add(a);
                        }
                }
                DeterministicSort(S_left);
                // System.out.printf("%d ", ai);
                DeterministicSort(S_right);
        }
}

public ArrayList CreateList(int n){
        ArrayList<Integer> S = new ArrayList<>();
        Random rand = new Random();
        for(int i = 0; i<n; i++) {
                S.add(rand.nextInt());
        }
        return S;
}

public static void main(String[] args){
        Quicksort sort = new Quicksort();
        int n = 100;
        System.out.println("Randomized");
        for (int i = 1; i<6; i++) {
                System.out.println("N =" + n);
                // creat n list
                ArrayList<Integer> S = sort.CreateList(n);
                // calculate execution time
                ArrayList<Long> time_list = new ArrayList<>();
                for (int j = 0; j<100; j++) {
                        long start = System.nanoTime();
                        sort.RandomizedSort(S);
                        long end = System.nanoTime();
                        time_list.add(end - start);
                }
                long avg_time = 0;
                for (int k = 0; k<100; k++) {
                        avg_time += time_list.get(k);
                }
                System.out.println("time: " + (avg_time/100));
                // next n
                n *= 10;
        }

        System.out.println("\nDeterministic");
        n = 10;
        for (int i = 1; i<6; i++) {
                System.out.println("N =" + n);
                // creat n list
                ArrayList<Integer> S = sort.CreateList(n);
                // calculate execution time
                ArrayList<Long> time_list = new ArrayList<>();
                for (int j = 0; j<100; j++) {
                        long start = System.nanoTime();
                        sort.DeterministicSort(S);
                        long end = System.nanoTime();
                        time_list.add(end - start);
                }
                long avg_time = 0;
                for (int k = 0; k<100; k++) {
                        avg_time += time_list.get(k);
                }
                System.out.println("time: " + (avg_time/100));
                // next n
                n *= 10;
        }
}
}
