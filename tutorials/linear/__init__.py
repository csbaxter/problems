import check50
import check50.c

@check50.check()
def exists():
    """linear.c exists."""
    check50.exists("linear.c")

@check50.check(exists)
def compiles():
    """linear.c compiles."""
    check50.c.compile("linear.c", lcs50=True)

@check50.check(compiles)
def score_50():
    """returns false for 50"""
    check50.run("./linear").stdin("50").stdout("Sorry better luck next time!\n").exit(0)
    

@check50.check(compiles)
def score_14():
    """returns true for 14"""
    check50.run("./linear").stdin("14").stdout("Found your number! Bingo!\n").exit(0)
