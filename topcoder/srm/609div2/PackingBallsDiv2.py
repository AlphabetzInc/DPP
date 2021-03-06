# -*- coding: utf-8 -*-

class PackingBallsDiv2:
    def minPacks(self, R, G, B):
        A = [R,G,B]
        c = 0
        A.sort()
        while A[2] > 3:
            A[2] -= 3
            c += 1
            A.sort()
        if A[2] == 2:
            c += 2
        elif A[2] == 3 and A[1] >= 2:
            c += 3
        elif A[2] == 3 and A[1] == 1:
            c += 2
        else:
            assert(A[2] == 1)
            c += 1
        return c

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

def do_test(R, G, B, __expected, caseNo):
    sys.stdout.write("  Testcase #%d ... " % caseNo)

    startTime = time.time()
    instance = PackingBallsDiv2()
    exception = None
    try:
        __result = instance.minPacks(R, G, B);
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
        R = 4
        G = 2
        B = 4
        __expected = 4

        # run the code
        return do_test(R, G, B, __expected, __no)

    if __no == 1:
        R = 1
        G = 7
        B = 1
        __expected = 3

        # run the code
        return do_test(R, G, B, __expected, __no)

    if __no == 2:
        R = 2
        G = 3
        B = 5
        __expected = 4

        # run the code
        return do_test(R, G, B, __expected, __no)

    if __no == 3:
        R = 78
        G = 53
        B = 64
        __expected = 66

        # run the code
        return do_test(R, G, B, __expected, __no)

    if __no == 4:
        R = 100
        G = 100
        B = 100
        __expected = 100

        # run the code
        return do_test(R, G, B, __expected, __no)

    # Your custom testcase goes here
    # if __no == 5 ...
    #     pass

def run_tests():
    sys.stdout.write("PackingBallsDiv2 (500 Points)\n\n")

    nPassed = nAll = 0
    if len(sys.argv) <= 1:
        for i in range(5):
            nAll += 1
            nPassed += run_testcase(i)
    else:
        for arg in sys.argv[1:]:
            nAll += 1
            nPassed += run_testcase(int(arg))

    sys.stdout.write("\nPassed : %d / %d cases\n" % (nPassed, nAll))

    T = time.time() - 1392483788
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
