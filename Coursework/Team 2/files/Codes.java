
public class Codes {
	private String routeName;
	private String routeCode;
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
	public Codes(String a, String b){
		this.routeCode = a;
		this.routeName = b;
	}
	public String toString(){
		return routeName + " " + routeCode;
	}

}
