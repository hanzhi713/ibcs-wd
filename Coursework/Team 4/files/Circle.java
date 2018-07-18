package javatest1;
public class Circle extends Shape{
    private double radius=1.0;
    public Circle(){
        super();
    }
    public Circle(double radius){
        super();
        this.radius = radius;
}
    public Circle(double radius, String color, boolean filled){
        super(color, filled);
        this.radius = radius;
}

	   public double getRadius() {
	      return this.radius;
	   }
	   public void setRadius(double radius) {
	      this.radius = radius;
	   }
	   public double getArea() {
		      return Math.PI * radius * radius;
		   }
	    public double getPerimeter(){
	        return Math.PI * radius * 2;
	    }
		public String toString() {
			   return "Circle[radius=" + radius + "]"; 
			}

}