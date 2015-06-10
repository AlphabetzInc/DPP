import java.io.PrintStream;
import java.util.Scanner;

import utils.Node;

/**
 * Created by Pankaj on 6/9/15.
 */
public class ReverseLinkedListIterative {

    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        PrintStream out = new PrintStream(System.out);

        int N = in.nextInt();
        int[] A = new int[N];
        for(int i=0;i<N;i++) A[i] = in.nextInt();
        Node head = new Node(A);
        out.println(head.toString());
        out.println(head.iReverse().toString());

        assert(head.iReverse().iReverse().equals(head));
    }
}
