public class Point2D {
   // Private instance variables
   private int x, y;

   // Constructors
   public Point2D() {  // default constructor
      this.x = 0;
      this.y = 0;
   }
   public Point2D(int x, int y) {
      this.x = x;
      this.y = y;
   }

   // Getters and Setters
   public int getX() {
      return this.x;
   }
   public void setX(int x) {
      this.x = x;
   }
   public int getY() {
      return this.y;
   }
   public void setY(int y) {
      this.y = y;
   }

   // Return "(x,y)"
   public String toString() {
      return "(" + this.x + "," + this.y + ")";
   }
}