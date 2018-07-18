
public class Temperaturetest {
	public static void main(String[] args) {
		Temperature a = new Temperature( 234,"Fahrenheit");
		System.out.println(a);
		a.toCelsius();
		System.out.println(a);
		a.toFahrenheit();
		System.out.println(a);
		a.raise(100);
		System.out.println(a);
		a.lower(100);
		System.out.println(a);

		
		
		
		
	}
}
