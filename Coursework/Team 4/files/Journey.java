
public class Journey {
	private String routeCode;
	private int delay;
	private boolean weatherRelated;
	
	public Journey(String routeCode,int delay,boolean weatherRelated){
		this.routeCode=routeCode;
		this.delay=delay;
		this.weatherRelated=weatherRelated;
	}
	
	public void setRouteCode(String routeCode){
		this.routeCode=routeCode;
	}
	public void setDelay(int delay){
		this.delay=delay;
	}
	public void setweatherRelated(boolean weatherRelated){
		this.weatherRelated=weatherRelated;
	}
	public String getRouteCode(){
		return this.routeCode;
	}
	public int getDelay(){
		return this.delay;
	}
	public boolean getweatherRelated(){
		return this.weatherRelated;
	}
}
