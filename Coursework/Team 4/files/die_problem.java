
public class die_problem {
	public static void main(String[] args){
		int[] RESULTS = new int[600];
		int a = 0;
		int b = 0;
		int c = 0;
		int d = 0;
		int e = 0;
		int f = 0;
		double lower = 0.147;
		double upper = 0.187;
		int high;
		int low;
		

	
		for(int i = 0; i<600;i++){
			int temp =(int)( Math.random()*6 +1);
			RESULTS[i] = temp;
			if(temp == 1){
				a = a+1;
			}
			else if(temp == 2){
				b = b+1;
			}
			else if(temp == 3){
				c = c+1;
			}
			else if(temp == 4){
				d = d+1;
			}
			else if(temp == 5){
				e = e+1;
			}
			else if(temp == 6){
				f = f+1;
			}
		
		
		}
		System.out.println("one:"+a+"two:"+b+"three:"+c+"four:"+d+"five:"+e+"six:"+f);
		high = (int)(600*upper);
		low = (int)(600*lower);
		if(low<a && a <high &&  low<b && b<high && low<c&& c<high && low<d&& d<high && low<e && e<high && low<f && f<high){
			System.out.println("unbiased");
		}
		else{
			System.out.println("biased");
		}
	

	}
}
