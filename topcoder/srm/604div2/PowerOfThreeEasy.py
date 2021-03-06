# -*- coding: utf-8 -*-

class PowerOfThreeEasy:
    def ableToGet(self, x, y):
        for k in xrange(30):
            i,j = x,y
            for l in xrange(k-1,-1,-1):
                if(i>j):
                    i -= pow(3,l)
                else:
                    j -= pow(3,l)
                if(i < 0 and j < 0):
                    break
                #print k,i,j
            if(i==0 and j==0):
                return "Possible"
        return "Impossible"

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys
import time

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            if abs(expected - received) < eps: return True
            if abs(received) > abs(expected) * (1.0 - eps) and abs(received) < abs(expected) * (1.0 + eps): return True
        else:
            return expected == received
    except:
        return False

def do_test(x, y, __expected, caseNo):
    sys.stdout.write("  Testcase #%d ... " % caseNo)

    startTime = time.time()
    instance = PowerOfThreeEasy()
    exception = None
    try:
        __result = instance.ableToGet(x, y);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + str(__expected) + "\n")
        sys.stdout.write("           Received: " + str(__result) + "\n")
        return 0

def run_testcase(__no):
    if __no == 0:
        x = 1
        y = 3
        __expected = "Possible"

        # run the code
        return do_test(x, y, __expected, __no)

    if __no == 1:
        x = 1
        y = 1
        __expected = "Impossible"

        # run the code
        return do_test(x, y, __expected, __no)

    if __no == 2:
        x = 3
        y = 0
        __expected = "Impossible"

        # run the code
        return do_test(x, y, __expected, __no)

    if __no == 3:
        x = 1
        y = 9
        __expected = "Impossible"

        # run the code
        return do_test(x, y, __expected, __no)

    if __no == 4:
        x = 3
        y = 10
        __expected = "Possible"

        # run the code
        return do_test(x, y, __expected, __no)

    if __no == 5:
        x = 1093
        y = 2187
        __expected = "Possible"

        # run the code
        return do_test(x, y, __expected, __no)

    if __no == 6:
        x = 0
        y = 0
        __expected = "Possible"

        # run the code
        return do_test(x, y, __expected, __no)

    # Your custom testcase goes here
    # if __no == 7 ...
    #     pass

def run_tests():
    sys.stdout.write("PowerOfThreeEasy (500 Points)\n\n")

    nPassed = nAll = 0
    if len(sys.argv) <= 1:
        for i in range(7):
            nAll += 1
            nPassed += run_testcase(i)
    else:
        for arg in sys.argv[1:]:
            nAll += 1
            nPassed += run_testcase(int(arg))

    sys.stdout.write("\nPassed : %d / %d cases\n" % (nPassed, nAll))

    T = time.time() - 1389459880
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
