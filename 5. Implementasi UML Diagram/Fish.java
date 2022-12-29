public class Fish extends Animal implements Pet {
    private String name;
  
    public Fish() {
      super(0);
    }
  
    @Override
    public String getName() {
      return name;
    }
  
    @Override
    public void setName(String name) {
      this.name = name;
    }
  
    @Override
    public void play() {
      // implementasi method play
      System.out.println("Ikan ini berenang");
    }
  
    @Override
    public void eat() {
      // implementasi method eat
      System.out.println("Ikan ini makan");
    }
  
    @Override
    public void walk() {
      System.out.println("Ikan ini berenang di laut");
    }
  }
  