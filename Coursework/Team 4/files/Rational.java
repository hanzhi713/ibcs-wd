public class Rational {
private int numerator; 
private int denominator; 

public Rational(){
	numerator = 0;
	denominator = 1;
}

public Rational(int n)
{ numerator = n;
 denominator = 1; }

public Rational(int numer, int denom)
{numerator = numer;
 denominator = denom;}

public int numerator()
{ return numerator; }

public int denominator()
{ return denominator; }


public Rational plus(Rational r) {
fixSigns();
r.fixSigns();
int denom = denominator * r.denominator;
int numer = numerator * r.denominator+ r.numerator * denominator; 
Rational rat = new Rational(numer, denom); 
rat.reduce();
return rat;
}

 private void fixSigns()
{ if (denominator <= 0){
	 System.exit(0); }
}
 private void reduce()
{int a = numerator;
int b = denominator;
while (a%b != 0){
	int temp = a%b;
	b = a;
	a = temp;}
}
}