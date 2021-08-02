import check50
import check50.c

@check50.check()
def exists():
    """mergesort.c exists."""
    check50.exists("mergesort.c")

@check50.check(exists)
def compiles():
    """mergesort.c compiles."""
    check50.c.compile("mergesort.c", lcs50=True)

@check50.check(compiles)
def does_it_work():
    """is it sorted correctly"""
    check50.run("./mergesort").stdout("0 1 2 3 4 5 6 7 8 9 \n").exit(0)
