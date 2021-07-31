import check50
import check50.c

@check50.check()
def exists():
    """calc.c exists."""
    check50.exists("calc.c")

@check50.check(exists)
def compiles():
    """calc.c compiles."""
    check50.c.compile("calc.c", lcs50=True)

@check50.check(compiles)
def problem_1():
    """+ - / 4 2 24 x 8 9"""
    check50.run("./calc + - / 4 2 24 x 8 9").stdout("50.000000").exit(0)

@check50.check(compiles)
def problem_2():
    """x - 3.4 5.6 7.9"""
    check50.run("./calc x - 3.4 5.6 7.9").stdout("-17.379999").exit(0)

@check50.check(compiles)
def problem_3():
    """+ 2 2"""
    check50.run("./calc + 2 2").stdout("4.000000").exit(0)

@check50.check(compiles)
def problem_4():
    """- 2 2"""
    check50.run("./calc - 2 2").stdout("0.000000").exit(0)
    
@check50.check(compiles)
def problem_5():
    """/ 2 2"""
    check50.run("./calc / 2 2").stdout("1.000000").exit(0)
    
@check50.check(compiles)
def problem_5():
    """% 2 2"""
    check50.run("./calc % 2 2").stdout("0.000000").exit(0)


 
