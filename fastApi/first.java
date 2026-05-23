public class first {

    public int add(int a,int b){
        return a + b;
    }
    public static void main(String[] args) {
        first f = new first();
        int sum = f.add(10, 20);
        System.out.println(sum);
    }
}
