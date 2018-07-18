package test1;

public class ManyDecks {
	private Deck[] allDecks;
	public static final int NUMDECKS = 500;

	/** constructor */
	public ManyDecks() {
		allDecks = new Deck[NUMDECKS];
		for (int i = 0; i < NUMDECKS; i++)
			allDecks[i] = new Deck();
	}

	/** Shuffle the Decks. */
	public void shuffleAll() {
		for (Deck d : allDecks)
			d.shuffle();

	}

	public void printDecks() {
		for (Deck d : allDecks)
			d.writeDeck();
	}
}