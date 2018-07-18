import java.util.Scanner;
public class BirthdayStuff {
	static java.util.Scanner in=new Scanner(System.in);
public static Date findBirthdate() {
	System.out.println("Enter birthdate: mo, day, yr: ");
	int m = in.nextInt();
	int d = in.nextInt();
	int y = in.nextInt();
	Date birthDate = new Date(m, d, y);
	return birthDate; }
public static void main(String[] args) {
             Date d1 = findBirthdate();
             Date d2 = new Date(d1.month(), d1.day(), d1.year());
             System.out.println(!(d1==d2));
} }