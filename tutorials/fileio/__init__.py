import check50
import check50.c

@check50.check()
def exists():
    """fileio.c exists"""
    check50.exists("fileio.c")

@check50.check(exists)
def compiles():
    """fileio.c compiles"""
    check50.c.compile("fileio.c", lcs50=True)

@check50.check(compiles)
def works_sentence():
    """handles copying source file to output file"""
    check50.run("./fileio anna.txt output.txt").exit(0)
    
@check50.check(compiles)
def works_sentence():
    """rejects improper command line input of no output file"""
    check50.run("./fileio anna.txt").stdout("Usage: fileio source dest\n").exit(1)
