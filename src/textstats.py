"""Small statistics over a text."""


def words(text):
    """The words of a text: runs of characters between white space."""
    return text.split()


def word_count(text):
    return len(words(text))


def average_word_length(text):
    """The mean length of the words of a text."""
    found = words(text)
    return sum(len(w) for w in found) / len(found)


def longest_word(text):
    """The longest word of a text; the first one when several are as long."""
    found = words(text)
    return max(found, key=len) if found else ""
