
public class TrainCompany {
	private String companyName;
	private static Codes c[];
	public String getCompanyName() {
		return companyName;
	}
	public static Codes[] getC() {
		return c;
	}
	public static void setC(Codes[] c) {
		TrainCompany.c = c;
	}
	public void setCompanyName(String companyName) {
		this.companyName = companyName;
	}
	public String getCompanyCode() {
		return companyCode;
	}
	public void setCompanyCode(String companyCode) {
		this.companyCode = companyCode;
	}
	private String companyCode;
	private int numberOfJourneys;
	private Journey[] journeyHistory = new Journey[100000];
	private String longestdelayname = null;
	
	public TrainCompany(String x, String y){
		this.companyName = x;
		this.companyCode = y;
		this.numberOfJourneys = 0;
	}
	public Journey getJourney(int x){
		return journeyHistory[x];
	}
	public void addJourney(Journey j){
		journeyHistory[numberOfJourneys] = j;
		numberOfJourneys++;
	}
	public double averageDelay(){
		double del = 0;
		int count = 0;
		for(Journey j : journeyHistory){
			if(j != null && !j.isWeatherRelated()){
				del += j.getDelay();
				count++;
	
			}
		}
		if(del == 0 && count == 0){
			return 0;
		}
		double avg_del = del/count;
		return avg_del;
	}
	public String longestDelay(){
		Journey longest = null ;
		int time = 0;
		for(Journey j : journeyHistory){
			if(j != null && !j.isWeatherRelated()){
				if(j.getDelay() > time){
					time = j.getDelay();
					longest = j;
				}
			}
		}
		String codemac = longest.getRouteCode();
		String name = null;
		for(Codes d : c){
			if(d != null && d.getRouteCode().equals(codemac)){
				name = d.getRouteName();
				break;
			}
		}
		longestdelayname = name;
		return longestdelayname;
	}
	public int getNumberOfJourneys() {
		return numberOfJourneys;
		
	}
	public String toString(){
		return companyName + ": Average Delay = " + averageDelay() + " : Longest Delay = " + longestdelayname;
	}
}

