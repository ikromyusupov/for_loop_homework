def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    a = ''
    for x in range(n):
        a += str(x) + ','
    return a[:-1]