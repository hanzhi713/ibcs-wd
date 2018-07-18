
public class Rationaltest {
	
	public static void main(String[] args) {
		Rational a = new Rational();
		System.out.println(a);
		Rational b = new Rational(4);
		System.out.println(b);
		Rational c = new Rational(4,2);
		System.out.println(c);
		System.out.println(c.numerator());
		System.out.println(c.denominator());
		System.out.println(b.plus(c));
		
		
		
	}
}
