import java.util.ArrayList;


public class Main {
	private static TrainCompany[] allCompanies = new TrainCompany[3];
	private static Codes[] allCodes = new Codes[10];
	private static ArrayList<Codes> newCodes = new ArrayList<Codes>();
	public static void main(String[] args){
		allCompanies[0] = new TrainCompany("Southern", "T290"); 
		allCompanies[1] = new TrainCompany("Northern","T400"); 
		allCompanies[2] = new TrainCompany("Eastern","T155");
		Journey s = new Journey("J100",3, false); 
		Journey t = new Journey("J103",8, true); 
		Journey u = new Journey("J104",10, true);
		allCompanies[0].addJourney(s); 
		allCompanies[1].addJourney(t); 
		allCompanies[0].addJourney(u); 
		allCompanies[0].addJourney(new Journey("J101",6, false));
		System.out.println(allCompanies[0].getCompanyCode());
		System.out.println(allCompanies[0].getJourney(1).getDelay());
		System.out.println(allCompanies[1].getNumberOfJourneys());
	
		allCompanies[1].addJourney(new Journey("A101", 10, false));
		allCompanies[1].addJourney(new Journey("A103", 30, false));
		allCompanies[1].addJourney(new Journey("A104", 60, false));
	
		allCodes[0] = new Codes("A101", "LHR - CDG");
		allCodes[1] = new Codes("A102", "LHR - AMS");
		allCodes[2] = new Codes("A102", "LHR - AMS");
		allCodes[3] = new Codes("A103", "LHR - FRA");
		allCodes[4] = new Codes("A104", "LHR - TXL");
		allCodes[5] = new Codes("A105", "LHR - ZRH");
		allCodes[6] = new Codes("A106", "LHR - MUC");
		allCodes[7] = new Codes("A107", "LHR - JFK");
		allCodes[8] = new Codes("A108", "LHR - HKG");
		allCodes[9] = new Codes("A109", "LHR - PVG");
		TrainCompany.setC(allCodes);
		System.out.println(allCompanies[1].averageDelay());
		System.out.println(allCompanies[1].longestDelay());
		
		convert();
		java.util.Iterator<Codes> itr = newCodes.iterator();
		while(itr.hasNext()){
			System.out.println(itr.next());
		}
	}
	public static void convert(){
		for(Codes c: allCodes){
			boolean duplication = false;
			for(Codes d : newCodes){
				if(d.getRouteCode().equals(c.getRouteCode())){
					duplication = true;
					break;
				}
			}
			if(!duplication){
				newCodes.add(c);
			}
		}
	}
}
