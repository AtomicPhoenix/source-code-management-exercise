def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    a = abs(a)
    b = abs(b)
    # Implement your solution here
    if a == 0 and b == 0:
        return None  # gcd(0,0) is undefined
    elif a == 0:
        return b
    elif b == 0:
        return a
    elif b > a:
        return gcd(b % a, a)
    else:
        return gcd(a % b, b)


def test_gcd(a: int, b: int, g: int | None):
    res = gcd(a, b)
    passed = "PASSED" if res == g else "FAILED"
    print(a, b, "\t|\t", g, "\t|\t", res, "\t|\t", passed)


print("\t\tGCD FUNCTION TESTS\t\t")
print("VALUES\t|    EXPECTED   |\tgcd()\t|\tTEST RESULT")
test_gcd(24, 54, 6)
test_gcd(-24, 54, 6)
test_gcd(7, 54, 1)
test_gcd(17, 34, 17)
test_gcd(34, 17, 17)
test_gcd(30, 0, 30)  # Any number times 0 = 0 so all numbers are factors of 0
test_gcd(0, 0, None)  # gcd(0,0) is undefined
test_gcd(100, 20, 20)
