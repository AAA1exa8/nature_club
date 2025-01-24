# Convert a list of tuples into a dictionary.
# Each tuple will have exactly two elements where the first element is the key and the second is the value.
# Use dict() constructor or a loop to convert the tuples into dictionary entries.
# [("a", 1), ("b", 2), ("c", 3)] -> {'a': 1, 'b': 2, 'c': 3}
# [("apple", "fruit"), ("cucumber", "vegetable")] -> {'apple': 'fruit', 'cucumber': 'vegetable'}
def tuples_to_dict(tuples: list) -> dict:
    return {}

# Merge two dictionaries into one.
# If there are overlapping keys, the values from the second dictionary should overwrite the first.
# Use .update() method or loop through the second dictionary.
# ({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) -> {'a': 1, 'b': 3, 'c': 4}
# ({}, {'x': 9}) -> {'x': 9}
def merge_dicts(dict1: dict, dict2: dict) -> dict:
    return {}

# Count the frequency of each character in a string.
# Return a dictionary with characters as keys and their counts as values.
# Use loop and check if the character is already a key in the dictionary.
# "abbccc" -> {'a': 1, 'b': 2, 'c': 3}
# "" -> {}
# "a" -> {'a': 1}
# "yatzee" -> {'y': 1, 'a': 1, 't': 1, 'z': 1, 'e': 2}
def char_frequency(s: str) -> dict:
    return {}

# Reverse a dictionary.
# Return a dictionary with keys and values swapped.
# Assume all values are unique so they can be used as keys.
# {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}
# {'apple': 'fruit', 'carrot': 'vegetable'} -> {'fruit': 'apple', 'vegetable': 'carrot'}
def reverse_dict(d: dict) -> dict:
    return {}

# Check if two dictionaries are equal.
# They are considered equal if they have the same key-value pairs.
# Use == or loop. 
# The function should return True if equal, otherwise False.
# ({'a': 1, 'b': 2}, {'a': 1, 'b': 2}) -> True
# ({'a': 1, 'b': 2}, {'a': 1, 'b': 3}) -> False
def are_dicts_equal(dict1: dict, dict2: dict) -> bool:
    return False

# Write a function to get the maximum value in a dictionary and its corresponding key.
# Return a tuple (key, max_value).
# Use max() function with the .items() method.
# {'a': 10, 'b': 20, 'c': 15} -> ('b', 20)
# {'mouse': 5, 'keyboard': 10, 'screen': 7} -> ('keyboard', 10)
def max_key_value(d: dict):
    return None

# Write a function to invert a dictionary with possible duplicate values.
# Keys should be gathered into a list if they have the same value.
# {'a': 1, 'b': 2, 'c': 1} -> {1: ['a', 'c'], 2: ['b']}
# {'x': 3, 'y': 3, 'z': 4} -> {3: ['x', 'y'], 4: ['z']}
def invert_dict_with_duplicates(d: dict) -> dict:
    return {}

# Check if a key exists in a dictionary.
# The function should return True if the key is present, otherwise False.
# Use 'in' operator or .get() method
# ({'a': 1, 'b': 2}, 'a') -> True
# ({'a': 1, 'b': 2}, 'c') -> False
def key_exists(d: dict, key) -> bool:
    return False

# Write a function to increment each value in a dictionary by a given number.
# Return the updated dictionary after incrementing.
# Use a loop or dictionary comprehension.
# ({'a': 1, 'b': 2}, 3) -> {'a': 4, 'b': 5}
# ({}, 5) -> {}
def increment_dict(d: dict, n: int) -> dict:
    return {}

# Write a function that returns all keys of a dictionary that map to a given value.
# Return a list of keys.
# Use a loop to gather keys.
# ({"a": 1, "b": 2, "c": 1, "d": 2}, 2) -> ['b', 'd']
# ({"x": 3, "y": 4, "z": 3}, 3) -> ['x', 'z']
def get_keys_for_value(d: dict, value) -> list:
    return []


# You don't need to pay attention to this
def print_red(s: str):
    print("\033[91m {}\033[00m".format(s))

def print_green(s: str):
    print("\033[92m {}\033[00m".format(s))


testNum = { 'tuples_to_dict': 0, 'merge_dicts': 0, 'char_frequency': 0, 'reverse_dict': 0, 'are_dicts_equal': 0, 'max_key_value': 0, 'invert_dict_with_duplicates': 0, 'key_exists': 0, 'increment_dict': 0, 'get_keys_for_value': 0 } 
def testAssert(testval, corval, testType: str):
    global testNum
    testNum[testType] += 1
    if testval == corval:
        print_green(f"Test {testNum[testType]} for {testType} passed")
    else:
        print_red(f"Test {testNum[testType]} for {testType} failed. Expected {corval} but got {testval}")

# Test cases for tuples_to_dict
testAssert(tuples_to_dict([("a", 1), ("b", 2), ("c", 3)]), {'a': 1, 'b': 2, 'c': 3}, 'tuples_to_dict')
testAssert(tuples_to_dict([("apple", "fruit"), ("cucumber", "vegetable")]), {'apple': 'fruit', 'cucumber': 'vegetable'}, 'tuples_to_dict')
testAssert(tuples_to_dict([]), {}, 'tuples_to_dict')

# Test cases for merge_dicts
testAssert(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 3, 'c': 4}, 'merge_dicts')
testAssert(merge_dicts({}, {'x': 9}), {'x': 9}, 'merge_dicts')
testAssert(merge_dicts({'p': 5}, {}), {'p': 5}, 'merge_dicts')

# Test cases for char_frequency
testAssert(char_frequency("abbccc"), {'a': 1, 'b': 2, 'c': 3}, 'char_frequency')
testAssert(char_frequency(""), {}, 'char_frequency')
testAssert(char_frequency("a"), {'a': 1}, 'char_frequency')
testAssert(char_frequency("yatzee"), {'y': 1, 'a': 1, 't': 1, 'z': 1, 'e': 2}, 'char_frequency')

# Test cases for reverse_dict
testAssert(reverse_dict({'a': 1, 'b': 2, 'c': 3}), {1: 'a', 2: 'b', 3: 'c'}, 'reverse_dict')
testAssert(reverse_dict({'apple': 'fruit', 'carrot': 'vegetable'}), {'fruit': 'apple', 'vegetable': 'carrot'}, 'reverse_dict')

# Test cases for are_dicts_equal
testAssert(are_dicts_equal({'a': 1, 'b': 2}, {'a': 1, 'b': 2}), True, 'are_dicts_equal')
testAssert(are_dicts_equal({'a': 1, 'b': 2}, {'a': 1, 'b': 3}), False, 'are_dicts_equal')
testAssert(are_dicts_equal({}, {}), True, 'are_dicts_equal')

# Test cases for max_key_value
testAssert(max_key_value({'a': 10, 'b': 20, 'c': 15}), ('b', 20), 'max_key_value')
testAssert(max_key_value({'mouse': 5, 'keyboard': 10, 'screen': 7}), ('keyboard', 10), 'max_key_value')

# Test cases for invert_dict_with_duplicates
testAssert(invert_dict_with_duplicates({'a': 1, 'b': 2, 'c': 1}), {1: ['a', 'c'], 2: ['b']}, 'invert_dict_with_duplicates')
testAssert(invert_dict_with_duplicates({'x': 3, 'y': 3, 'z': 4}), {3: ['x', 'y'], 4: ['z']}, 'invert_dict_with_duplicates')

# Test cases for key_exists
testAssert(key_exists({'a': 1, 'b': 2}, 'a'), True, 'key_exists')
testAssert(key_exists({'a': 1, 'b': 2}, 'c'), False, 'key_exists')
testAssert(key_exists({}, 'a'), False, 'key_exists')

# Test cases for increment_dict
testAssert(increment_dict({'a': 1, 'b': 2}, 3), {'a': 4, 'b': 5}, 'increment_dict')
testAssert(increment_dict({}, 5), {}, 'increment_dict')
testAssert(increment_dict({'m': -1, 'n': 0}, 2), {'m': 1, 'n': 2}, 'increment_dict')

# Test cases for get_keys_for_value
testAssert(get_keys_for_value({"a": 1, "b": 2, "c": 1, "d": 2}, 2), ['b', 'd'], 'get_keys_for_value')
testAssert(get_keys_for_value({"x": 3, "y": 4, "z": 3}, 3), ['x', 'z'], 'get_keys_for_value')
testAssert(get_keys_for_value({}, 1), [], 'get_keys_for_value')
