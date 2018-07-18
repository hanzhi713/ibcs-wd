public class TrainCompany {
	private String companyName;
	private String companyCode;
	private int numberOfJourneys;
	public Journey[] journeyHistory = new Journey[100000];
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
	public TrainCompany(String x, String y){
		this.companyName = x;
		this.companyCode = y;
		this.numberOfJourneys = 0;
	}
	public void addJourney(Journey j){
		journeyHistory[numberOfJourneys] = j;
		numberOfJourneys ++;
	}
	public double averageDelay(){
		int delayTotal = 0;
		int count = 0;
		for (int x = 0; x<numberOfJourneys; x++){
			if(!journeyHistory[x].getWeatherRelated()){
				delayTotal =  (delayTotal + journeyHistory[x].getDelay());
				count++;
			}
		}
		return (double)(delayTotal)/count;
	}
	public String longestDelay(Codes[] c){
		String route = "";
		String maxCode = "";
		int maxDelay = -1;
		for (int x = 0; x < numberOfJourneys; x++){
			if ((journeyHistory[x].getDelay() > maxDelay) && (!journeyHistory[x].getWeatherRelated())){
				maxDelay = journeyHistory[x].getDelay();
				maxCode = journeyHistory[x].getRouteCode();
			}
		}
		for (int y = 0; y<c.length; y++){
			if(c[y] != null){
				if(c[y].getRouteCode() == maxCode){
					route = c[y].getRouteName();
				}
			}
		}
		return route;
	}
	public String toString(Codes[] c){
		String d = companyName;
		double e = averageDelay();
		String f = longestDelay(c);
		String result = d + " : Average Delay = " + e + " : Longest Delay = " + f;
		return result;
	}
}
