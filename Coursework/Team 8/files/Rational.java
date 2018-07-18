public class Rational {
	private int numerator; 
	private int denominator;
	public Rational(){
		numerator=0;
		denominator=1;}
	/** Constructs a Rational with numerator n and * denominator 1. */
	Rational(int n){
		numerator=n;
		denominator=1;}
	/** Constructs a Rational with specified numerator and * denominator.*/
	Rational(int numer, int denom){
		numerator=numer;
		denominator=denom;}
	/** @return numerator */
	int numerator(){
		return numerator; }
	public void set_numer(int plus){
		numerator=plus;
	}
	/** @return denominator */
	int denominator(){
		return denominator; }
	public void set_denom(int plus){
		denominator=plus; }
	/** Returns (this + r). Leaves this unchanged.
	 * @return this rational number plus r
	 * @param r a rational number to be added to this Rational */
	public Rational plus(Rational r) { 
		Rational result = new Rational(this.denominator()*r.numerator()+this.numerator()*r.denominator(),this.denominator()*r.denominator());
		return result;}
	public Rational times(Rational r) { 
		Rational result = new Rational(this.numerator()*r.numerator(),this.denominator()*r.denominator());
		return result;}
	public Rational minus(Rational r) { 
		Rational result = new Rational(this.numerator()*r.denominator()-this.denominator()*r.numerator(),this.denominator()*r.denominator());
		return result;}
	public Rational divide(Rational r) { 
		Rational result = new Rational(this.numerator()*r.denominator(),this.denominator()*r.numerator());
		return result;}
	void fixSigns(){
		if (denominator<0){
			denominator*=-1;
			numerator*=-1;
		}
	}
	void reduce(){
		int a=numerator;
		int b=denominator;
		while (a%b!=0){
			int temp = a%b;
			a=b;
			b=temp;
		}
		numerator/=b;
		denominator/=b;
	}
	public String toString(){
		return (numerator+"/"+denominator);
	}
}
