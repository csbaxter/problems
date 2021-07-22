import check50
import check50.c

@check50.check()
def exists():
    """linear.c exists."""
    check50.exists("simulate.c")
    check50.exists("monte_hall.c")

@check50.check(exists)
def compiles():
    """linear.c compiles."""
    check50.c.compile("simulate.c", lcs50=True)
    check50.c.compile("monte_hall.c", lcs50=True)