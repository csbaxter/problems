import check50
import check50.c

@check50.check()
def exists():
    """binary.c exists."""
    check50.exists("binary.c")

@check50.check(exists)
def compiles():
    """binary.c compiles."""
    check50.c.compile("binary.c", lcs50=True)

@check50.check(compiles)
def does_it_work20():
    """does it find the number"""
    check50.run("./binary").stdin("20").stdout("Found\n").exit(0)
    
@check50.check(compiles)
def does_it_work4():
    """does it find the number"""
    check50.run("./binary").stdin("4").stdout("Found\n").exit(0)

@check50.check(compiles)
def does_it_work18():
    """does it find the number"""
    check50.run("./binary").stdin("18").stdout("Found\n").exit(0)
    
@check50.check(compiles)
def does_it_work99():
    """does it find the number"""
    check50.run("./binary").stdin("99").stdout("Not found!\n").exit(0)
    
@check50.check(compiles)
def does_it_work1():
    """does it find the number"""
    check50.run("./binary").stdin("1").stdout("Not found!\n").exit(0)
