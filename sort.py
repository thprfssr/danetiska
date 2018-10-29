alphabet = "абгдеѳийклмнопрстуўфх"
macron = "\u0304"
types = ["m", "f", "n", "v", "adj", "pn", "pp", "adv", "c", "num"]

def letter_ordinal(letter):
    n = len(alphabet)
    for i in range(n):
        if alphabet[i] == letter:
            break
    if letter in alphabet:
        return i
    if letter not in alphabet:
        return -1

def is_valid_word(word):
    for letter in word:
        if letter not in alphabet + macron:
            print("Error: Invalid word! Use the Danetish alphabet")
            quit()
    return True

def is_less_than(word_a, word_b):
    is_valid_word(word_a)
    is_valid_word(word_b)

    tmp_a = word_a.replace(macron, "")
    tmp_b = word_b.replace(macron, "")
    len_a = len(tmp_a)
    len_b = len(tmp_b)
    n = min(len_a, len_b)
    for i in range(n):
        letter_a = tmp_a[i]
        letter_b = tmp_b[i]
        n_a = letter_ordinal(letter_a)
        n_b = letter_ordinal(letter_b)
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
