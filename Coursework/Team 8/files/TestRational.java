
public class TestRational {

	public static void main(String[] args) {
		Rational half = new Rational();
		System.out.println(half);
		half.set_numer(1);
		half.set_denom(2);
		System.out.println(half);
		Rational thirds = new Rational(1,3);
		System.out.println(half.plus(thirds));
		Rational diff = null;
		diff=thirds.minus(half);
		diff.set_denom(diff.denominator()*-1);
		diff.set_numer(diff.numerator()*-1);
		System.out.println(diff);
		diff.fixSigns();
		System.out.println(diff);
		Rational one = null;
		Rational half2 = new Rational(half.numerator(),half.denominator());
		one = half.plus(half2);
		System.out.println(one);
		one.reduce();
		System.out.println(one);
	}

}
