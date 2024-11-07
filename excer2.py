# You'll get a string like this "[1, 2, 3, 4, 5]" and you need to return a list of numbers.
# Use .trim() to remove the brackets and then use .split(",") to get a list of strings.
# int() will convert a string to a number.
# "[1]" -> [1] 
# "[1, 2, 3, 4, 5]" -> [1, 2, 3, 4, 5]
# "[]" -> []
def parse_list_of_nums(s: str) -> list:
    return []


# Use function parse_list_of_nums to get a list of numbers and then sum the elements of the list.
# "[1, 2, 3, 4, 5]" -> 15
# "[]" -> 0
# "[1]" -> 1
def parse_and_sum(s: str) -> int:
    return 0


# Remove duplicates from a list.
# Use in operator
# if x in lst:
# x in lst returns true if x is in the list
# use second list
# [1, 2, 3, 4, 4, 5, 5, 6] -> [1, 2, 3, 4, 5, 6]
# [1, 1, 1, 1, 1, 1, 1, 1] -> [1]
# [1, 3, 1, 3, 1, 3, 1, 3] -> [1, 3]
def remove_duplicates(lst: list) -> list:
    return []


# Count vowels in a string
# use in operator
def vowels(s: str) -> int:
    vowels_lst = ['a', 'e', 'i', 'o', 'u']
    return 0


# Compress a string like this "aaabbbcc" -> "a3b3c2"
# use one variable to keep track of the current character
# use another variable to keep track of the count of the current character
# the compressed string will be saved in third variable
# aaabbbcc -> a3b3c2
# 1111 -> 14
# ababab -> ababab
# "" -> ""
# a -> a
# aa -> a2
def compress(s: str) -> str:
    return ''

# Your input will look like this "Game 43: red 1, blue 2, green 3; red 2, blue 2, green 3"
# Return True if in any of the rounds of the game any team scored more then 20 points.
# Use multiple .split() calls to remove "Game x: " and then split the games into rounds and roundes into scores.
# Use int() to convert the scores to numbers.
# You will have to use multiple loops inside each other
# Game 43: red 1, blue 2, green 3; red 2, blue 2, green 3 -> False
# Game 4: red 1, blue 2, green 3; red 2, blue 2, green 23 -> True
# Game 5000: red 19, blue 19, green 19; red 19, blue 19, green 19 -> False
def parse_game(s: str) -> bool:
    return False


# Check if the string is balanced. A string is balanced if it has the same number of opening and closing brackets.
# () -> True
# ( -> False
# ()() -> True
# (()) -> True
# (() -> False
# ())(
def is_balanced(s: str) -> bool:
    return False


# Parse time in the format "HH:MM:SS" and return the number of seconds.
# Use .split() to get a list of strings.
# Use int() to convert the strings to numbers.
# 1:00:00 -> 3600
# 1:01:01 -> 3661
# 5:24:12 -> 19452
def parse_time(tm: str) -> int:
    return 0


# Count the number of unique characters in a string.
# Use in operator, .append() and len()
# Use a list to keep track of the unique characters
# "a" -> 1
# "aa" -> 1
# "ab" -> 2
# "abc" -> 3
# "abcabc" -> 3
# "" -> 0
# "hello world" -> 8
def unique_chars(s: str) -> int:
    return 0


# You don't need to pay attention to this
def print_red(s: str):
    print("\033[91m {}\033[00m".format(s))

def print_green(s: str):
    print("\033[92m {}\033[00m".format(s))


testNum = {'parse_list_of_nums': 0, 'parse_and_sum': 0, 'remove_duplicates': 0, 'vowels': 0, 'compress': 0, 'parse_game': 0, 'is_balanced': 0, 'parse_time': 0, 'unique_chars': 0}
def testAssert(testval, corval, testType: str):
    global testNum
    testNum[testType] += 1
    if testval == corval:
        print_green(f"Test {testNum[testType]} for {testType} passed")
    else:
        print_red(f"Test {testNum[testType]} for {testType} failed. Expected {corval} but got {testval}")



testAssert(parse_list_of_nums("[1, 2, 3, 4, 5]"), [1, 2, 3, 4, 5], 'parse_list_of_nums')
testAssert(parse_list_of_nums("[1]"), [1], 'parse_list_of_nums')
testAssert(parse_list_of_nums("[]"), [], 'parse_list_of_nums')
testAssert(parse_list_of_nums("[100, 200, 300]"), [100, 200, 300], 'parse_list_of_nums')

# Test cases for parse_and_sum
testAssert(parse_and_sum("[1, 2, 3, 4, 5]"), 15, 'parse_and_sum')
testAssert(parse_and_sum("[]"), 0, 'parse_and_sum')
testAssert(parse_and_sum("[1]"), 1, 'parse_and_sum')
testAssert(parse_and_sum("[10, 20, 30]"), 60, 'parse_and_sum')

# Test cases for remove_duplicates
testAssert(remove_duplicates([1, 2, 3, 4, 4, 5, 5, 6]), [1, 2, 3, 4, 5, 6], 'remove_duplicates')
testAssert(remove_duplicates([1, 1, 1, 1, 1, 1]), [1], 'remove_duplicates')
testAssert(remove_duplicates([1, 3, 1, 3, 1, 3]), [1, 3], 'remove_duplicates')
testAssert(remove_duplicates([]), [], 'remove_duplicates')

# Test cases for vowels
testAssert(vowels("hello"), 2, 'vowels')
testAssert(vowels("world"), 1, 'vowels')
testAssert(vowels("aeiou"), 5, 'vowels')
testAssert(vowels("xyz"), 0, 'vowels')

# Test cases for compress
testAssert(compress("aaabbbcc"), "a3b3c2", 'compress')
testAssert(compress("1111"), "14", 'compress')
testAssert(compress("ababab"), "ababab", 'compress')
testAssert(compress(""), "", 'compress')
testAssert(compress("a"), "a", 'compress')
testAssert(compress("aa"), "a2", 'compress')

# Test cases for parse_game
testAssert(parse_game("Game 43: red 1, blue 2, green 3; red 2, blue 2, green 3"), False, 'parse_game')
testAssert(parse_game("Game 4: red 1, blue 2, green 3; red 2, blue 2, green 23"), True, 'parse_game')
testAssert(parse_game("Game 5000: red 19, blue 19, green 19; red 19, blue 19, green 19"), False, 'parse_game')
testAssert(parse_game("Game 1: red 21; blue 5"), True, 'parse_game')

# Test cases for is_balanced
testAssert(is_balanced("()"), True, 'is_balanced')
testAssert(is_balanced("("), False, 'is_balanced')
testAssert(is_balanced("()()"), True, 'is_balanced')
testAssert(is_balanced("(())"), True, 'is_balanced')
testAssert(is_balanced("(()"), False, 'is_balanced')
testAssert(is_balanced("())("), False, 'is_balanced')

# Test cases for parse_time
testAssert(parse_time("1:00:00"), 3600, 'parse_time')
testAssert(parse_time("1:01:01"), 3661, 'parse_time')
testAssert(parse_time("5:24:12"), 19452, 'parse_time')
testAssert(parse_time("0:00:01"), 1, 'parse_time')

# Test cases for unique_chars
testAssert(unique_chars("a"), 1, 'unique_chars')
testAssert(unique_chars("aa"), 1, 'unique_chars')
testAssert(unique_chars("ab"), 2, 'unique_chars')
testAssert(unique_chars("abc"), 3, 'unique_chars')
testAssert(unique_chars("abcabc"), 3, 'unique_chars')
testAssert(unique_chars(""), 0, 'unique_chars')
testAssert(unique_chars("hello world"), 8, 'unique_chars')
