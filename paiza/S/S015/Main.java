import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int k = Integer.parseInt(scan.next());
        int s = Integer.parseInt(scan.next());
        int t = Integer.parseInt(scan.next());

        scan.close();

        Main main = new Main();
        String res = "";
        res = main.insert(k, res);
        System.out.println(res.substring(s - 1, t));
    }

    public String insert(int k, String res){
        k -= 1;
        if(k==0){
            res = "ABC";
        }else{
            res = "A" + insert(k, res) + "B" + insert(k, res) + "C";
        }
        return res;
    }
}
