import check50
import check50.c

@check50.check()
def exists():
    """affine.c exists."""
    check50.exists("affine.c")

@check50.check(exists)
def compiles():
    """affine.c compiles."""
    check50.c.compile("affine.c", lcs50=True)

@check50.check(compiles)
def encrypts_a_as_i():
    """encrypts "a" as "i" using "a=5" "b=8" as key"""
    check50.run("./affine").stdin("5").stdin("8").stdin("a").stdout("[Cc]iphertext:\s*i\n", "ciphertext: i\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_niphaa():
    """encrypts "barfoo" as "niphaa" using "a=5" "b=8" as key"""
    check50.run("./affine").stdin("5").stdin("8").stdin("barfoo").stdout("[Cc]iphertext:\s*niphaa\n", "ciphertext: niphaa\n").exit(0)

@check50.check(compiles)
def encrypts_BARFOO_as_NIPHAA():
    """encrypts "BARFOO" as "NIPHAA" using "a=5" "b=8" as key"""
    check50.run("./affine").stdin("5").stdin("8").stdin("BARFOO").stdout("[Cc]iphertext:\s*NIPHAA\n", "ciphertext: NIPHAA\n").exit(0)

@check50.check(compiles)
def encrypts_BaRFoo_OhWQbb():
    """encrypts "BaRFoo" as "OhWQbb" using "a=7" "b=7" as key"""
    check50.run("./affine").stdin("7").stdin("7").stdin("BaRFoo").stdout("[Cc]iphertext:\s*OhWQbb\n", "ciphertext: OhWQbb\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_ihymvv():
    """encrypts "barfoo" as "ihymvv" using "a=27" "b=7" as key"""
    check50.run("./affine").stdin("27").stdin("7").stdin("barfoo").stdout("[Cc]iphertext:\s*ihymvv\n", "ciphertext: ihymvv\n").exit(0)

@check50.check(compiles)
def checks_for_handling_non_alpha():
    """encrypts "world, say hello!" as "iadxp, emk tqxxa!" using "a=27" "b=7" as key"""
    check50.run("./affine").stdin("27").stdin("7").stdin("world, say hello!").stdout("[Cc]iphertext:\s*dvysk, zhf olssv!\n", "ciphertext: dvysk, zhf olssv!\n").exit(0)

