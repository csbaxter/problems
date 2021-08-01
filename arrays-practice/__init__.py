import check50
import check50.c

@check50.check()
def exists():
    """all files exist."""
    check50.exists("countdown.c")
    check50.exists("fibo.c")
    check50.exists("garbage.c")
    check50.exists("initializations.c")
    check50.exists("mean.c")
    check50.exists("minesweeper.c")
    check50.exists("pokemon.c")

@check50.check(exists)
def compiles():
    """all files compile."""
    check50.c.compile("affine.c", lcs50=True)
    check50.c.compile("fibo.c", lcs50=True)
    check50.c.compile("garbage.c", lcs50=True)
    check50.c.compile("initializations.c", lcs50=True)
    check50.c.compile("mean.c", lcs50=True)
    check50.c.compile("minesweeper.c", lcs50=True)
    check50.c.compile("pokemon.c", lcs50=True)
