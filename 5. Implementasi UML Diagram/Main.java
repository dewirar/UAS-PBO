public class Main {
    public static void main(String[] args) {
      Fish f = new Fish();
      Cat c = new Cat("Veyy");
      Animal a = new Fish();
      Animal s = new Spider();
      Pet p = new Cat();

      //spider
      s.eat();
      s.walk();
      System.out.println("++++++++++++++++++++++++++++++");

      //cat
      c.getName();
      c.play();
      c.eat();
      c.walk();
      System.out.println("++++++++++++++++++++++++++++++");

      //fish
      f.setName("Lynn");
      f.play();
      f.walk();
      f.eat();
      System.out.println("++++++++++++++++++++++++++++++");

    }
  }
  