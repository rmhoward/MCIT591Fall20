def isTriangular(x):
    """Returns whether or not a given number x is triangular and the position of the triangular number. (As a tuple)

    If it's not triangular, it returns 0 for position.

    The triangular number Tn is a number that can be represented in the form of a triangular grid of
    points where the first row contains a single element and
    each subsequent row contains one more element than the
    previous one.

    We can just use the fact that the nth triangular
    number can be found by using a formula: Tn = n(n + 1) / 2.

    Example: 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)

    Example: 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)
    """
    list = []
    number = int((x - 1) * x / 2)

    if (x == number) or (x == 2):
        value = True
        list.append(value)
        answer = x - 1
        list.append(answer)


    else:
        list.append(False)
        list.append(0)


    return tuple(list)

print(isTriangular(2))