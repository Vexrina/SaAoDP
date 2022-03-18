import java.util.Arrays;
import java.util.Scanner;

public class Lab01 {
    public static void main(String[] args) {
        int Col = 6;
        int Row = 5;
        int min_limit = -250;
        final int variant = 24;
        int max_limit = 1000 + variant;
        int[][] mtx = generateMtx(min_limit, max_limit, Row, Col);
        System.out.println("Not sort mtx: ");
        outputMtx(mtx, Row, Col);
        System.out.println("Choose sort method: 1- sel, 2 - ins, 3 - bubble, 4 - shell, 5 - tournament, 6 - quick, 7 - heap, 8 - all timers.");
        short choosen;
        choosen = 7;
        switch (choosen) {
            case 1:
                sel_sort(mtx, Col, Row);
            case 2:
                ins_sort(mtx, Row, Col);
            case 3:
                bubble_sort(mtx, Row, Col);
            case 4:
                shell_sort(mtx, Row, Col);
            case 5:
                //tournament_sort(mtx, Row, Col);
            case 6: {
                int low;
                int high;
                low = 0;
                high = Col - 1;
                for (int i = 0; i < Row; i++)
                    quick_sort(mtx, Col, low, high, i);
                outputMtx(mtx, Row, Col);
            }
            case 7: {
                for (int i = 0; i < Row; i++)
                    Heapsort(mtx[i]);
                outputMtx(mtx, Row, Col);
            }

        }
    }

    //Help func
    public static int[][] generateMtx(int min, int max, int row, int col) {
        int[][] result;
        result = new int[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                result[i][j] = min + (int) (Math.random() * max);
            }
        }
        return result;
    }

    public static void outputMtx(int[][] mtx, int row, int col) {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print(mtx[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void swap(int[][] mtx, int i, int j, int Row) {
        int tmp = mtx[Row][i];
        mtx[Row][i] = mtx[Row][j];
        mtx[Row][j] = tmp;
    }

    public static void heapify(int arr[], int n, int i) {
        int largest = i; // Инициализируем наибольший элемент как корень
        int l = 2 * i + 1; // левый = 2*i + 1
        int r = 2 * i + 2; // правый = 2*i + 2

        // Если левый дочерний элемент больше корня
        if (l < n && arr[l] > arr[largest])
            largest = l;

        // Если правый дочерний элемент больше, чем самый большой элемент на данный момент
        if (r < n && arr[r] > arr[largest])
            largest = r;
        // Если самый большой элемент не корень
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            // Рекурсивно преобразуем в двоичную кучу затронутое поддерево
            heapify(arr, n, largest);
        }
    } // help funk for HeapSort

    //sort's
    public static void sel_sort(int mtx[][], int col, int row) {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                int minInd = j;
                for (int k = j; k < col; k++) {
                    if (mtx[i][k] < mtx[i][minInd]) {
                        minInd = k;
                    }
                }
                swap(mtx, j, minInd, i);
            }
        }
        outputMtx(mtx, row, col);
    }

    public static void ins_sort(int mtx[][], int row, int col) {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                int value = mtx[i][j];
                int k = j - 1;
                for (; k >= 0; k--) {
                    if (value < mtx[i][k]) {
                        mtx[i][k + 1] = mtx[i][k];
                    } else {
                        break;
                    }
                }
                mtx[i][k + 1] = value;
            }
        }
        outputMtx(mtx, row, col);
    }

    public static void bubble_sort(int mtx[][], int row, int col) {
        for (int i = 0; i < row; i++) {
            boolean flag = true;
            while (flag) {
                flag = false;
                for (int j = 1; j < col; j++) {
                    if (mtx[i][j] < mtx[i][j - 1]) {
                        swap(mtx, j, j - 1, i);
                        flag = true;
                    }
                }
            }
        }
        outputMtx(mtx, row, col);
    }

    public static void shell_sort(int mtx[][], int row, int col) {
        for (int i = 0; i < row; i++) {
            int gap = col / 2;
            while (gap >= 1) {
                for (int j = 0; j < col; j++) {
                    for (int k = j - gap; k >= 0; k -= gap) {
                        if (mtx[i][k] > mtx[i][k + gap])
                            swap(mtx, k, k + gap, i);
                    }
                }
                gap /= 2;
            }
        }
        outputMtx(mtx, row, col);
    }

    public static void quick_sort(int mtx[][], int col, int low, int high, int row) {
        if (low >= high)
            return;
        int middle = low + (high - low) / 2;
        int opora = mtx[row][middle];
        int i = low, j = high;
        while (i <= j) {
            while (mtx[row][i] < opora)
                i++;
            while (mtx[row][j] > opora)
                j--;
            if (i <= j) {
                swap(mtx, i, j, row);
                j--;
                i++;
            }
        }
        if (low < j)
            quick_sort(mtx, col, low, j, row);
        if (high > i)
            quick_sort(mtx, col, i, high, row);
    }

    public static void Heapsort(int arr[]) {
        int n = arr.length;

        // Построение кучи (перегруппируем массив)
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);

        // Один за другим извлекаем элементы из кучи
        for (int i = n - 1; i >= 0; i--) {
            // Перемещаем текущий корень в конец
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Вызываем процедуру heapify на уменьшенной куче
            heapify(arr, i, 0);
        }
    }

    public static int[] tournament_sort(int[] arr) {//очень плохо, неповторять в домашних условиях.
        int step = 0; int stepLose = 0;
        if (arr.length < 7)
            Heapsort(arr);
        else {
            String[] newArray, winners, losers;
            newArray = new String[arr.length];
            losers = new String[arr.length];
            winners = new String[arr.length];
            for(int i=0; i<arr.length;i++)
                newArray[i]=Integer.toString(arr[i]);
            if(Integer.parseInt(buildThree(newArray))<Integer.parseInt(winners[step])) {
                losers[stepLose] = buildThree(newArray);
                stepLose++;
            }
            else {
                winners[step] = buildThree(newArray);
                step++;
            }
        }
        return null;
    }
    public static String buildThree(String[] arr) {
        String[] Three;
        Three = new String[7];
        for(int i=0; i<4;i++)
            Three[i] = arr[i];
        Three[4]=Integer.toString(compare(Integer.parseInt(Three[1]),Integer.parseInt(Three[0])));
        Three[5]=Integer.toString(compare(Integer.parseInt(Three[2]),Integer.parseInt(Three[3])));
        Three[6]=Integer.toString(compare(Integer.parseInt(Three[4]),Integer.parseInt(Three[5])));
        return Three[6];
    }

    public static int compare(int num1, int num2) {
        if (num1 > num2) return num2;
        else return num1;
    }
}