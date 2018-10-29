cyrillic_alphabet = "абгдеѳийклмнопрстуўфх"
latin_alphabet = "abgdeθijklmnoprstuwφx"
macron = "\u0304"
types = ["m", "f", "n", "adj", "pn", "v", "pp", "adv", "c", "num"]

def letter_ordinal(letter, alphabet):
    n = len(alphabet)
    for i in range(n):
        if alphabet[i] == letter:
            break
    if letter in alphabet:
        return i
    if letter not in alphabet:
        #print("Error: Invalid letter! Use the Danetish Alphabet!")
        #quit()
        return -1

def is_valid_word(word, alphabet):
    for letter in word:
        if letter not in alphabet + macron:
            #print("Error: Invalid word! Use the Danetish alphabet")
            #quit()
            return False
    return True

def is_less_than(word_a, word_b, alphabet):
    is_valid_word(word_a, alphabet)
    is_valid_word(word_b, alphabet)

    tmp_a = word_a.replace(macron, "")
    tmp_b = word_b.replace(macron, "")
    len_a = len(tmp_a)
    len_b = len(tmp_b)
    n = min(len_a, len_b)
    for i in range(n):
        letter_a = tmp_a[i]
        letter_b = tmp_b[i]
        n_a = letter_ordinal(letter_a, alphabet)
        n_b = letter_ordinal(letter_b, alphabet)
        if n_a < n_b:
            return True
        if n_a > n_b:
            return False
        if n_a == n_b:
            continue

    if tmp_a == tmp_b:
        if macron in word_a and macron not in word_b:
            return False
        if macron not in word_a and macron in word_b:
            return True
        if macron in word_a and macron in word_b:
            n_a = word_a.index(macron)
            n_b = word_b.index(macron)
            return n_a > n_b

def translate(word, alphabet_a, alphabet_b):
    is_valid_word(word, alphabet_a)
    string = ""
    for letter in word:
        if letter == macron:
            string += macron
        else:
            n = letter_ordinal(letter, alphabet_a)
            string += alphabet_b[n]
    return string

def is_valid_entry(entry, alphabet):
    array = entry.split()
    if len(array) < 3:
        return False
    word = array[0]

    wordtype = array[1]
    wordtype = wordtype.replace("(", "")
    wordtype = wordtype.replace("):", "")
    is_valid_word(word, alphabet)
    if wordtype not in types:
        #print("Error: Not a valid word type!")
        #quit()
        return False
    else:
        return True

def get_dictionary_entries(filename):
    f = open("dictionary.txt", "r")
    string = f.read()
    array = string.splitlines()
    return array

def get_word(entry):
    array = entry.split()
    return array[0]

def get_wordtype(entry):
    array = entry.split()
    return array[1]

def get_definition(entry):
    array = entry.split()
    definition = " ".join(array[2:])
    return definition

def is_list_ordered(array):
    b = True
    n = len(array)
    for i in range(n - 1):
        entry = array[i]
        next_entry = array[i + 1]
        word = get_word(entry)
        next_word = get_word(next_entry)
        if not is_less_than(word, next_word, latin_alphabet):
            return False
    return True

def sort(array):
    n = len(array)
    while not is_list_ordered(array):
        for i in range(n - 1):
            entry = array[i]
            next_entry = array[i + 1]
            word = get_word(entry)
            next_word = get_word(next_entry)
            if not is_less_than(word, next_word, latin_alphabet):
                array[i + 1] = entry
                array[i] = next_entry
    return array

array = get_dictionary_entries("dictionary.txt")
for entry in array:
    entry = entry.replace("ā", "a" + macron)
    entry = entry.replace("ē", "e" + macron)
    entry = entry.replace("ī", "i" + macron)
    entry = entry.replace("ō", "o" + macron)
    entry = entry.replace("ū", "u" + macron)
    b = is_valid_entry(entry, latin_alphabet)
    if b:
        word = get_word(entry)
        #word = translate(word, latin_alphabet, cyrillic_alphabet)
        wordtype = get_wordtype(entry)
        definition = get_definition(entry)
        print(word, wordtype, definition)


array = get_dictionary_entries("txt")
array = sort(array)
