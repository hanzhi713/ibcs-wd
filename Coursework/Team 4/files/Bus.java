
public class Bus extends Journey {
	private String routeCode;
	private int delay;
	private boolean weatherRelated;
	public Bus(String routeCode, int delay, boolean weatherRelated) {
		super(routeCode, delay, weatherRelated);
		// TODO Auto-generated constructor stub
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
