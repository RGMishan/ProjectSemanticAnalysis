punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(oldS):
    for i in punctuation_chars:
        oldS = str(oldS).replace('%s' % i, '')
    return oldS
