
public class puzzel {
	public static void main(String[] args){
		int a = 0;
		int n = 7;
		int b = (n-1)/2 ;
		int[] temp = new int[2];
		int[][] PUZZLE = new int[n][n];
		for(int i = 1; i< n*n+1; i++){

			if( a == -1){
				a = n -1;
			}
			if (b == n){
				b = 0;
			}
			if(PUZZLE[a][b]>0){
				a = temp[0]+1;
				b = temp[1];
			}
			PUZZLE[a][b] = i;
			temp[0] = a;
			temp[1] = b;
			a = a -1;
			b = b +1;
		}
		for(int s = 0;s<n;s++){
			for(int w = 0;w<n;w++){
				System.out.print(s + "  " + w+"  ");
				System.out.println(PUZZLE[s][w]);

			}
		}

		
		
	}
}
