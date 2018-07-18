package javatest1;

public class Rectangle extends Shape{
    private double width = 1.0;
    private double Length = 1.0;
    public Rectangle(){
        super();
    }
    public Rectangle(double width, double height){
        super();
        this.width = width;
        this.Length = height;
    }
    public Rectangle(double width, double height, String color, boolean Filled){
        super(color, Filled);
        this.width = width;
        this.Length = height;
    }
    public double getWidth(){
        return width;
    }
    public double getLength(){
        return Length;
    }
    public void setWidth(double width){
        this.width = width;
    }
    public void setLength(double height){
        this.Length = height;
    }
    public double getArea(){
        return width * Length;
    }
    public double getPerimeter(){
        return (width+Length)*2;
    }
    public String toString(){
        return "Rectangle[width = "+ width+"]";
}
}
