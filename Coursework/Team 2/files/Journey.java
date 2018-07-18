
public class Journey {
	private String routeCode;
	private int delay;
	private boolean weatherRelated;
	public String getRouteCode() {
		return routeCode;
	}
	public void setRouteCode(String routeCode) {
		this.routeCode = routeCode;
	}
	public int getDelay() {
		return delay;
	}
	
	public void setDelay(int delay) {
		this.delay = delay;
	}
	public boolean isWeatherRelated() {
		return weatherRelated;
	}
	public void setWeatherRelated(boolean weatherRelated) {
		this.weatherRelated = weatherRelated;
	}
	public Journey(String routeCode, int delay, Boolean weatherRelated){
		this.routeCode = routeCode;
		this.delay = delay;
		this.weatherRelated = weatherRelated;
	}
	
}
