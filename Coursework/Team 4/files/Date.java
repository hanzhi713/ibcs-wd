public class Date {
private int day; 
private int month;
private int year;
public Date() {
	day = 0;
	month = 0;
	year = 0;
	
 }
public Date(int mo, int da, int yr) {
	day = da;
	month = mo;
	year = yr;
 }
public int month() {
	return month;
}
public int day() {
	return day;
 }
public int year() {
	return year;
 }

public String toString(){
	System.out.println(month + "/" + day + "/" + year);
	return null;

 }
}