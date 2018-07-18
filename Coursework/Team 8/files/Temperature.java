public class Temperature {
	private String scale; //valid values are "F" or "C" private double degrees;
	private double degrees;
/** constructor with specified degrees and scale */
	public Temperature(double tempDegrees, String tempScale) {
		degrees = tempDegrees; scale = tempScale;}
/** Mutator. Converts this Temperature to degrees Fahrenheit.
* Precondition: Temperatureisavalidtemperature
* in degrees Celsius.
* @return this temperature in degrees Fahrenheit
*/
	public Temperature toFahrenheit() { 
		if (scale=="C"){
			degrees=degrees*1.8+32;
			scale="F";}
			return this;
	}
/** Mutator. Converts this Temperature to degrees Celsius.
* Precondition: Temperatureisavalidtemperature
* in degrees Fahrenheit.
* @return this temperature in degrees
*/
	public Temperature toCelsius(){
		if (scale=="F"){
			degrees=(degrees-32)*5/9;
			scale="C";}
			return this;
	}
/** Mutator.
* @param amt the number of degrees to
* @return this temperature raised by amt degrees */
	public  Temperature raise(double amt) {
		degrees+=amt;
		return this;}
/** Mutator.
* @param amt the number of degrees
* @return this temperature lowered */
	public Temperature lower(double amt) { return this.raise(-amt); }
/** @param tempDegrees the number of
* @param tempScale the temperature
* @return true if tempDegrees is a
* in the given temperature scale, false otherwise */
	public static boolean isValidTemp(double tempDegrees, String tempScale){
		if (tempScale=="C"){
			boolean flag = tempDegrees>-273.15;
			return (flag);
		} 
		else{
			boolean flag = tempDegrees>-459.67;
			return (flag);
		}
	}
}