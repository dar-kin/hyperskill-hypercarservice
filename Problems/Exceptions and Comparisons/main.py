class WordError(Exception):
    pass


def check_w_letter(word):
    if "w" in word:
        raise WordError
    return word
