
public class Main {
	
	
	public static void main(String... args){
		TrainCompany[] allCompanies = new TrainCompany[3];
		allCompanies[0]=new TrainCompany("Southern","T290");
		allCompanies[1]=new TrainCompany("Northern","T400");
		allCompanies[2]=new TrainCompany("Eastern","T155");
		
		Journey s = new Journey("J100",3,false);
		Journey t = new Journey("J103",8,true);
		Journey u = new Journey("J104",10,true);
		
		allCompanies[0].addJourney(s);
		allCompanies[1].addJourney(t);
		allCompanies[0].addJourney(u);
		allCompanies[0].addJourney(new Journey("J101",6,false));
		System.out.println(allCompanies[0].getCompanyCode());
		System.out.println(allCompanies[0].getJourney(1).getDelay());
		System.out.println(allCompanies[1].getNumberOfJourneys());
		
	}
	public static Codes[] convert(Codes[]c){
		int count = 0;
		Codes[] converted = new Codes[c.length];
		for(int i = 0; i<c.length;i++ ){
			boolean Duplication = false;
			for(int j=0;j<converted.length;j++){
				if(c[i].getRouteCode()==converted[j].getRouteCode()){
					Duplication=true;
				}
			}
			if(Duplication==false){
				converted[count]=c[i];
				count++;
			}
			
		}
		return converted;
		
	}
	


}
