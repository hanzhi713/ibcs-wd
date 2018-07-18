
public class TrainCompany {
	private String companyName;
	private String companyCode;
	private int numberOfJourneys;
	private Journey[] JourneyHistory=new Journey[100000];
	
	public TrainCompany(String x, String y){
		this.companyName = x;
		this.companyCode = y;
		this. numberOfJourneys=0;
	}
	
	public TrainCompany(){}
	
	Journey getJourney(int x){
		return JourneyHistory[x];
	}
	
	public void addJourney(Journey j){
		JourneyHistory[numberOfJourneys]=j;
		numberOfJourneys++;
	}
	public double averageDelay(){
		int delayTotal=0;
		int count = 0;
		for(int i = 0;i<numberOfJourneys; i++){
			if(!JourneyHistory[i].getweatherRelated()){
				delayTotal=delayTotal + JourneyHistory[i].getDelay();
				count++;
			}
		}
		return (delayTotal)/count;
	}
	public String LongestDelay(Codes[] c){
		String route = "";
		String maxCode="";
		int maxDelay = -1;
		for(int i = 0; i<numberOfJourneys; i++){
			if((JourneyHistory[i].getDelay()>maxDelay&&(!JourneyHistory[i].getweatherRelated()))){
				maxDelay = JourneyHistory[i].getDelay();
				maxCode=JourneyHistory[i].getRouteCode();
			}	
		}
		for (int j=0;j<c.length;j++){
			if(c[j].getRouteCode()==maxCode){
				route=c[j].getRouteName();
			}
		}
		return route;
	}
	
	public String toString(Codes[] c){
		double a=averageDelay();
		String b= LongestDelay(c);
		return("Eastern:Average Delay = "+ a +"minutes:Longest Delay ="+b);
	}

	public String getCompanyName() {
		return companyName;
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

	public int getNumberOfJourneys() {
		return numberOfJourneys;
	}

	public void setNumberOfJourneys(int numberOfJourneys) {
		this.numberOfJourneys = numberOfJourneys;
	}

	public Journey[] getJourneyHistory() {
		return JourneyHistory;
	}

	public void setJourneyHistory(Journey[] journeyHistory) {
		JourneyHistory = journeyHistory;
	}
	

}
