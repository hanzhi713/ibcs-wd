
public class jus_puzzle {
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
		int num = 0;
		for(int e = 0;e<n;e++){
			num = num+ PUZZLE[e][e];
			
		}
		for(int d = 0; d<n;d++){
			int u = 0;
			for(int t=0;t<n;t++){
				u = u + PUZZLE[d][t];

			}	
		 	if (u!=num){
			System.out.println("wrong");
			}
		for(int q = 0; q<n;q++){
			int w = 0;
			for(int y=0;y<n;y++){
				w = w + PUZZLE[y][q];

			}
			if (w!=num){
			System.out.println("wrong");
			}
			
			
		}
		int fia = 0;
		for(int z=0;z<n;z++){
			fia = fia + PUZZLE[n-1-z][n-1-z];
		}
		if(fia!=num){
			System.out.println("wrong");
		}
		


	}

	}
}

