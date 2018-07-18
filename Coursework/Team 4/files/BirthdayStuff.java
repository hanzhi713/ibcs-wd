import java.util.Scanner;
public class BirthdayStuff {
    private static Scanner num = new Scanner(System.in); 
	
public static Date findBirthdate() {
	
	System.out.println("Enter birthdate: mo, day, yr: ");
	int m =  num.nextInt();
	int d = num.nextInt();
	int y =  num.nextInt();
	Date birthDate = new Date(m, d, y);
return birthDate; }

public static void main(String[] args) {
             Date d = findBirthdate();
             System.out.println(d);

} }
