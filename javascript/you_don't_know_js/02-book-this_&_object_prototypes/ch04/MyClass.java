import java.lang.*;

public class MyClass {

    public static void main(String args[])
    {
        int i = 1;
        Integer i_obj = new Integer(2);
        System.out.println("Hello.");
        System.out.println("Integer class: " + (i_obj instanceof Integer));
        // won't even compile - requires references, found int
        // unlike the statement in the Chapter 4, not entirely everything
        // in Java is an object
        System.out.println("int primitive: " + (i instanceof Integer));
    }
}

