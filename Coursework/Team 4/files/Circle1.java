package test1;

public class Circle1 {
	   // private instance variables
	   private double radius;
	   private String color;

	   // Constructors
	   public Circle1() {
	      this.radius = 1.0;
	      this.color = "red";
	   }
	   public Circle1(double radius) {
	      this.radius = radius;
	      this.color = "red";
	   }
	   public Circle1(double radius, String color) {
	      this.radius = radius;
	      this.color = color;
	   }

	   // Getters and Setters
	   public double getRadius() {
	      return this.radius;
	   }
	   public String getColor() {
	      return this.color;
	   }
	   public void setRadius(double radius) {
	      this.radius = radius;
	   }
	   public void setColor(String color) {
	      this.color = color;
	   }

	   // Describle itself
	   public String toString() {
	      return "Circle[radius=" + radius + ",color=" + color + "]";
	   }

	   // Return the area of this Circle
	   public double getArea() {
	      return radius * radius * Math.PI;
	   }
	}