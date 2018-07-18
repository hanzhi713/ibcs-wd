public class Journey {
	private String routeCode;
	private int delay;
	private boolean weatherRelated;
	public Journey(String x, int y, boolean z){
		this.routeCode = x;
		this.delay = y;
		this.weatherRelated = z;
	}
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
	public boolean getWeatherRelated() {
		return weatherRelated;
	}
	public void setWeatherRelated(boolean weatherRelated) {
		this.weatherRelated = weatherRelated;
	}

}
