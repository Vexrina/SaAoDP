import java.util.Arrays;

public class Quest {
    public static void main(String[] args) {
        int N = 168;
        First(N);
        int[] Array;
        final int K = 10;
        final int max = 9;
        final int min = 1;
        Array = new int[K];
        createArray(Array,K, min, max);
        triangle(new int[]{17,19,55});
        maxNum(K,Array);
    }
    public static void First(int N){
        if(N%3==0){
            System.out.println(3);
        }
        else if(N%2!=0){
            simpleNumbers(N);
        }
        else if(N%2==0&&N%4!=0)
        {
            simpleNumbers(N);
        }
        else if(N%4==0){
            System.out.println(4);
        }
    }
    public static void simpleNumbers(int N){
        for (int d = 5; d<Math.sqrt(N); d++) {
            if(N%d==0)
                System.out.println(d);
        }
    }
    public static void triangle(int Array[]){
        Arrays.sort(Array);
        boolean flag = true;
        for(int i= 9; i>=2; i--){
            for(int j=8; j>=1; j--){
                for(int k=7;k>=0;k--){
                    if(Array[k]+Array[j]>Array[i] && Array[k]+Array[i]>Array[j] && Array[j]+Array[i]>Array[k] && flag){
                        int per= Array[k]+Array[j]+Array[i];
                        flag = false;
                        System.out.println( per + " = Summ (" + Array[k] + Array[j] +Array[i]);
                        break;
                    }
                }
            }
        }
        if(flag)
            System.out.println(0);
    }
    public static void createArray(int Array[], int K,int max, int min){
        for(int i = 0; i<K; i++){
            Array[i] = 5 + (int) (Math.random() * 17);
        }
    }
    public static boolean hasNum(int number,int find) {
       while(number>0){
           if(number%10 == find)
               return true;
           else
               number/=10;
       }
       return false;
    }
    public static void maxNum(int K, int Array[]){
        String result ="";
        int[] Result;
        Result = new int[K];
        int point = -1;
        for(int j = 9; j>=0; j--) {
            for (int i = K - 1; i >= 0; i--) {
                if (hasNum(Array[i], j)) {
                    point++;
                    Result[point] = Array[i];
                }
            }
        }
        for(int i = 0; i<K;i++){
            result+= String.valueOf(Result[i]);
        }
        System.out.println(result);
    }
}
