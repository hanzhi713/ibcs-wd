public class Temperature {
private String scale;//valid values are "F" or "C" 
private double degrees;

/** constructor with specified degrees and scale */
public Temperature(double tempDegrees, String tempScale) 
{degrees = tempDegrees;
scale = tempScale;}


public Temperature toFahrenheit() 
{ this.degrees  = this.degrees*1.8 +32;
this.scale = "Fahrenheit";

return this;}


public Temperature toCelsius()
{ this.degrees  = (this.degrees - 32)*(5/9) ;
this.scale = "Celsius";

return this;}


public Temperature raise(double amt) 
{this.degrees = this.degrees +amt;
return this;}


public Temperature lower(double amt)
{ {this.degrees = this.degrees -amt;
return this;} }

public static void isValidTemp(double tempDegrees, String tempScale)

{ if(tempScale =="Celsius" ){
	if( tempDegrees >= -273){
		System.out.println(true);}
	else{
		System.out.println(false);}
	}
if(tempScale =="Fahrenheit" ){
	if( tempDegrees >= 0){
		System.out.println(true);}
	else{
		System.out.println(false);}
	}
	}
}

