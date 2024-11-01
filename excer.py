def sum_to_n(n: int) -> int:

def factorial(n: int) -> int:
    
vowels_lst = ['a', 'e', 'i', 'o', 'u']
def vowels(s: str) -> int:
    global vowels_lst


def reverse(s: str) -> str:

def maximum(lst: list) -> int:


# Don't care about the code below this line
testNum = {'sum_to_n': 0, 'factorial': 0, 'vowels': 0, 'reverse': 0, 'maximum': 0}
def testAssert(testval, corval, testType: str):
    global testNum
    testNum[testType] += 1
    if testval == corval:
        print("Test", testNum[testType], testType, "Passed")
    else:
        print("Test", testNum[testType], testType, "Failed")


testAssert(sum_to_n(5), 15, 'sum_to_n')
testAssert(sum_to_n(10), 55, 'sum_to_n')
testAssert(sum_to_n(0), 0, 'sum_to_n')

testAssert(factorial(5), 120, 'factorial')
testAssert(factorial(10), 3628800, 'factorial')
testAssert(factorial(0), 1, 'factorial')

testAssert(vowels('hello'), 2, 'vowels')
testAssert(vowels('aeiou'), 5, 'vowels')
testAssert(vowels('hll'), 0, 'vowels')

testAssert(reverse('hello'), 'olleh', 'reverse')
testAssert(reverse('aeiou'), 'uoiea', 'reverse')
testAssert(reverse('hll'), 'llh', 'reverse')

testAssert(maximum([1, 2, 3, 4, 5]), 5, 'maximum')
testAssert(maximum([1, 2, 3, 4, 5, 10]), 10, 'maximum')
testAssert(maximum([1, 2, 3, 4, 5, 10, 0]), 10, 'maximum')





