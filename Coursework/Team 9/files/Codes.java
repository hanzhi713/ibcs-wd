public class Codes {
	private String routeName;
	private String routeCode;
	
	public Codes(String a, String b){
		this.routeName = a;
		this.routeCode = b;
	}

	public String getRouteName() {
		return routeName;
	}

	public void setRouteName(String routeName) {
		this.routeName = routeName;
	}

	public String getRouteCode() {
		return routeCode;
	}

	public void setRouteCode(String routeCode) {
		this.routeCode = routeCode;
	}

}
