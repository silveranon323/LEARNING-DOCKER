import java.util.Properties;

public class Test {
    public static void systemProperties() {
        Properties prop = System.getProperties();
        System.out.println(prop);

    }

    public static void main(String[] args) {
        systemProperties();
    }
}