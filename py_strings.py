def reverse(text: str) -> str:
    """
    Return the 'text' backwards.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The text written backwards.
    """
    return text[::-1]


def first_to_upper(text: str) -> str:
    """
    Changes each first character of the word to uppercase.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The modified text
    """
    lista = ""
    for word in text.split():
    	lista+=word[0].upper()+word[1:]+' '
    return lista[0:-1]


def count_vowels(text: str) -> int:
    """
    Counts number of vovels in the text.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    inp
        Number of vowels.
    """
    vowels = "aeiouyAEIOUYąęóĄĘÓ"
    liczba = len([char for char in text if char in vowels])
    return liczba


def sum_digits(text: str) -> int:
    """
    Finds all digitts in the text and returns its sum.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int
        Sum of all digits in the text.
    """
    cyfry = '0123456789'
    tab_cyfry = [char for char in text if char in cyfry]
    tab_cyfry_wartosc = list(map(int,tab_cyfry))
    return sum(tab_cyfry_wartosc)


def search_substr(text: str, sub: str) -> int:
    """
    Search for sub(string) in the text. Returns the position or None.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int or None
        Position of the sub(string) or None.
    """
    miejsce = text.find(sub)
    if miejsce == -1: return None
    else: return miejsce
