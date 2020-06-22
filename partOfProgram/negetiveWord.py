punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(oldS):
    for i in punctuation_chars:
        oldS = str(oldS).replace('%s' % i, '')
    return oldS

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(str):
    str = strip_punctuation(str).split()
    k = 0
    for i in str:
        if i in negative_words:
            k += 1
    return k

