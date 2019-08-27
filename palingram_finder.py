import sys

def load(file):
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text if len(x) > 1]
            return loaded_text
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)

def load_reverse(file):
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower()[::-1] for x in loaded_text if len(x) > 1]
            return loaded_text
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error, invalid number of arguments")
        sys.exit(1)
    
    palindromes = []
    words = load(sys.argv[1])
    reverse_words = load_reverse(sys.argv[1])

    for word in words:
        if word[:] == word[::-1]:
            palindromes.append(word)
    x = 0
    words_containing_palindromes = []
    grams = []
    for word in words:
        for p in palindromes:
            if word.__contains__(p):
                # words_containing_palindromes.append(word)
                other_part = word.replace(p, '')
                if other_part in reverse_words:
                    # if palindrome is the beginning part of the word
                    if word[:len(p)] == p:
                        grams.append(other_part[::-1] + p + other_part)
                    else:
                        grams.append(other_part + p + other_part[::-1])

    print(f"Out of {len(words)} words in the text file, there are {len(palindromes)} palindromes\n")    
    print(f"{len(grams)} palingrams were found\n")
    print(grams)
