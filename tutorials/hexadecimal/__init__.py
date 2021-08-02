import check50
import check50.c

@check50.check()
def exists():
    """hexadecimal.c exists."""
    check50.exists("hexadecimal.c")

@check50.check(exists)
def compiles():
    """hexadecimal.c compiles."""
    check50.c.compile("hexadecimal.c", lcs50=True)
