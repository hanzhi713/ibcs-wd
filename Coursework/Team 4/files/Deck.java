package test1;

public class Deck {
	private int[] deck;
	public static final int NUMCARDS = 52;

	public Deck() {
		deck = new int[NUMCARDS];
		for (int i = 0; i < NUMCARDS; i++)
			deck[i] = i;
	}

	public void writeDeck() {
		for (int card : deck)
			System.out.print(card + " ");
		System.out.println();
		System.out.println();
	}

	private void swap(int[] arr, int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	public void shuffle() {
		int index;
		for (int i = NUMCARDS - 1; i > 0; i--) {
			index = (int) (Math.random() * (i + 1));
			swap(deck, i, index);
		}
	}
}
