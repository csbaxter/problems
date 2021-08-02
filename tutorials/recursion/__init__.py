import check50
import check50.c

@check50.check()
def exists():
    """recursion.c exists."""
    check50.exists("mystruct.c")

@check50.check(exists)
def compiles():
    """recursion.c compiles."""
    check50.c.compile("recursion.c", lcs50=True)
