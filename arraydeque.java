
import java.util.ArrayDeque;

public class arraydeque {
    public static void main(String[] args) {
        ArrayDeque <Integer> ad1 = new ArrayDeque<>();
        ad1.add(5);
        ad1.add(67);
        ad1.add(53);

        ad1.addLast(50);

        System.out.println("Array Deque :" + ad1);
        System.out.println(ad1.getFirst());
        System.out.println(ad1.contains(67));
    }
}
