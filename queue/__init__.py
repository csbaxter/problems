import check50
import check50.c

@check50.check()
def exists():
    """stack.c exists."""
    check50.exists("queue.c")

@check50.check(exists)
def compiles():
    """queue.c compiles."""
    check50.c.compile("queue.c", lcs50=True)
