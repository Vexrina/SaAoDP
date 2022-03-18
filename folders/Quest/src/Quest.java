import java.util.Arrays;

public class Quest {
    public static void main(String[] args) {
        int N = 168;
        First(N);
        int[] Array;
        final int K = 10;
        final int max = 15;
        final int min = 1;
        Array = new int[K];
        createArray(Array, max, min);
        maxNum(Array);
      //  triangle(Array);
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
        for(int i = Array.length-1; i>=2; i--){
            for(int j=Array.length-2; j>=1; j--){
                for(int k=Array.length-3;k>=0;k--){
                    if(Array[k]+Array[j]>Array[i] && Array[k]+Array[i]>Array[j] && Array[j]+Array[i]>Array[k] && flag){
                        int per= Array[k]+Array[j]+Array[i];
                        flag = false;
                        System.out.println( per + " = Summ (" + Array[k] +" + "+ Array[j] + " + " +Array[i] + ")");
                        break;
                    }
                }
            }
        }
        if(flag)
            System.out.println(0);
    }
    public static void createArray(int Array[],int max, int min){
        for(int i = 0; i<Array.length; i++){
            Array[i] = min + (int) (Math.random() * max);
        }
        System.out.println(Arrays.toString(Array));
    }
    public static void maxNum(int Array[]){
        String[] temp;
        Arrays.sort(Array);
        temp = new String[Array.length];
        for(int i = 0; i<temp.length; i++){
            temp[i]=String.valueOf(Array[i]);
        }
        System.out.println(Arrays.toString(temp));
        String[] newArr;
        newArr = new String[temp.length];
        for(int i = 0; i<newArr.length;i++){
            for(int j = newArr.length-1; j>=0; j--){
                int lenght = temp[j].length();
                if(temp[j].length()==1){
                    if(temp[j].equals("9")) {
                        newArr[i] = temp[j];
                        temp[j] = "";
                        break;
                    }
                }
            }
        }
        int q;
        q = 0;
        for(int i = 0; i < newArr.length; i++){
            for(int j = 1; j < temp[newArr.length-1].length(); j++){
                for(int k = 9; k>0; k--){
                    if(temp[q].length()==j && temp[q].equals(Integer.toString(k))){
                        newArr[i]=temp[q];
                        temp[q] ="";
                        break;
                    }
                }
                break;
            }
            q++;
        }
        System.out.println(Arrays.toString(newArr));
        System.out.println(Arrays.toString(temp));
    }
    public static void nameword(String s){
        if(s.length()==1){

        }
        else {

        }
    }
}
