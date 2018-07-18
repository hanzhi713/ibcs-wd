import random
import time

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for i in range(len(xs)):
       if xs[i]== target:
           return i
    return -1

def search_binary_iter(xs, target):
    """ Find and return the index of key in sequence xs """

	
	
	
	

def search_binary_recur(xs, target):







def find_unknown_words(vocab, wds,method):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    if method == 1:
        for w in wds:
            if (search_linear(vocab, w) < 0):
                result.append(w)
    else:
        vocab.sort()
        if method == 2:
            for w in wds:
                if (search_binary_recur(vocab, w) < 0):
                    result.append(w)
        else:
            for w in wds:
                if (search_binary_iter(vocab, w) < 0):
                    result.append(w)
    return result


def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """
    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


bigger_vocab = load_words_from_file("vocab.txt")
print("There are {0} words in the vocab, starting with\n {1} "
      .format(len(bigger_vocab), bigger_vocab[:6]))

book_words = get_words_in_book("alice_in_wonderland.txt")
print("There are {0} words in the book, the first 100 are\n{1}".
           format(len(book_words), book_words[:100]))

# t0 = time.clock()
# missing_words = find_unknown_words_linear(bigger_vocab, book_words)
# t1 = time.clock()
# print("Search linear: There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))
t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words,1)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))