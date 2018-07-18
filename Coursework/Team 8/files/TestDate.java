
public class TestDate {
	public static void addCentury(Date recent, Date old) {
        old.addYears(100);
        recent = old;
        /*This shouldn't work!*/}
	public static void main(String[] args) {
		Date oldDate = new Date(1, 13, 1900);
		Date recentDate = null;
		addCentury(recentDate, oldDate);
		System.out.println(recentDate);
	}

}
