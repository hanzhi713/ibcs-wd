package test1;
public class Point3D extends Point2D {
	   // Private instance variables
	   private int z;

	   // Constructors
	   public Point3D() {  // default constructor
	      super();     // x = y = 0
	      this.z = 0;
	   }
	   public Point3D(int x, int y, int z) {
	      super(x, y);
	      this.z = z;
	   }

	   // Getters and Setters
	   public int getZ() {
	      return this.z;
	   }
	   public void setZ(int z) {
	      this.z = z;
	   }

	   // Return "(x,y,z)"
	   @Override
	   public String toString() {
	      return "(" + super.getX() + "," + super.getY() + "," + this.z + ")";
	   }
	}