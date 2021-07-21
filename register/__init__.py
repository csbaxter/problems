import check50
import check50.c


@check50.check()
def exists():
    """register.c exists"""
    check50.exists("register.c")


@check50.check(exists)
def compiles():
    """register.c compiles"""
    check50.c.compile("register.c", lcs50=True)


@check50.check(compiles)
def test041():
    """input of 1.00 for cost and 1.41 paid yields output of 4"""
    check50.run("./register").stdin("1.00").stdin("1.41").stdout(coins(4), "4\n").exit(0)


@check50.check(compiles)
def test001():
    """input of 1.00 for cost and 1.01 paid yields output of 1"""
    check50.run("./register").stdin("1.00").stdin("1.01").stdout(coins(1), "1\n").exit(0)


@check50.check(compiles)
def test015():
    """input of 1.85 for cost and 2.00 paid yields output of 2"""
    check50.run("./register").stdin("1.85").stdin("2.00").stdout(coins(2), "2\n").exit(0)


@check50.check(compiles)
def test160():
    """input of 4.40 cost and 6.00 paid yields output of 7"""
    check50.run("./register").stdin("4.40").stdin("6.00").stdout(coins(7), "7\n").exit(0)


@check50.check(compiles)
def test230():
    """input of 20.00 cost and 43.00 paid yields output of 92"""
    check50.run("./register").stdin("20.00").stdin("43.00").stdout(coins(92), "92\n").exit(0)


@check50.check(compiles)
def test420():
    """input of 4.2 yields output of 18"""
    from re import search
    expected = "18\n"
    actual = check50.run("./register").stdin("20.00").stdin("24.20").stdout()
    if not search(coins(18), actual):
        help = None
        if search(coins(22), actual):
            help = "did you forget to round your input to the nearest cent?"
        raise check50.Mismatch(expected, actual, help=help)


@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("./register").stdin("-1").reject()


@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./register").stdin("foo").reject()


@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("./register").stdin("").reject()


def coins(num):
    # regex that matches `num` not surrounded by any other numbers (so coins(2) won't match e.g. 123)
    return fr"(?<!\d){num}(?!\d)"
