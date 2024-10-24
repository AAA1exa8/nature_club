from warnings import warn


def variables():
    print("variables() called")
    print("variables are used to store data in code.")
    print("variables are like boxes that store data.")
    print("variables have a name and a value.")
    print("variables can be assigned a value using the = operator.")
    print("x = 5")
    x = 5
    print("x is", x)
    print("variables can be reassigned a value.")
    print("x = 10")
    x = 10
    print("x is", x)
    print("variables can be used in expressions.")
    print("y = 5")
    y = 5
    print("x + y is", x + y)
    print("x - y is", x - y)
    print("x * y is", x * y)
    print("x / y is", x / y)
    print("x // y is", x // y)
    print("x % y is", x % y)
    print("x ** y is", x ** y)
    print("variables can be used in strings.")
    print("name = 'John'")
    name = "John"
    print("Hello, " + name + "!")
    print("variables can be used in lists.")
    print("numbers = [1, 2, 3, 4, 5]")
    numbers = [1, 2, 3, 4, 5]
    print("numbers is", numbers)
    print("variables can be used in dictionaries.")
    print("person = {'name': 'John', 'age': 25}")
    person = {'name': 'John', 'age': 25}
    print("person is", person)
    print("variables can be used in functions.")
    def add(x, y):
        return x + y
    print("""
def add(x, y):
    return x + y
    """)
    print("add(5, 10) is", add(5, 10))




def if_statements():
    print("if_stateents() called")
    print("if statements are used to make decisions in code.")
    # print("we write if bool:")
    # print("    code")
    # print("elif bool:")
    # print("    code")
    # print("else:")
    # print("    code")
    print("""
we write
if bool:
    code
elif bool:
    code
else:
    code
    """)
    print("where bool is a boolean expression")
    print("classic boolean expressions:")
    true = True
    false = False
    print("True and True is", true and true)
    print("True and False is", true and false)
    print("False and False is", false and false)
    print("True or True is", true or true)
    print("True or False is", true or false)
    print("False or False is", false or false)
    print("not True is", not true)
    print("not False is", not false)
    x = 5
    y = 10
    print("x = 5")
    print("y = 10")
    print("x == y is", x == y)
    print("x != y is", x != y)
    print("x < y is", x < y)
    print("x > y is", x > y)
    print("x <= y is", x <= y)
    print("x >= y is", x >= y)
    print("x is y is", x is y)
    print("x is not y is", x is not y)
    print("x in [1, 2, 3] is", x in [1, 2, 3])
    print("x not in [1, 2, 3] is", x not in [1, 2, 3])
    # if statements
    print("""
x = 5
y = 10
if x == y:
    print("x == y")
else :
    print("x != y")
    """)
    print("outputs:")
    if x == y:
        print("x == y")
    else :
        print("x != y")
        
    print("""
x = 5
y = 5
if x < y:
    print("x < y")
elif x > y:
    print("x > y")
else:
    print("x == y")
    """)
    print("outputs:")

    x = 5
    y = 5
    if x < y:
        print("x < y")
    elif x > y:
        print("x > y")
    else:
        print("x == y")


def loops():
    print("loops() called")
    print("loops are used to repeat code.")
    print("while loops:")
    print("""
i = 0
while i < 5:
    print(i)
    i += 1
    """)
    print("outputs:")
    i = 0
    while i < 5:
        print(i)
        i += 1
    print("for loops:")
    print("for loops create local named variable.")
    print("this variable gains the value of each element in the iterable.")
    print("""
for i in range(5):
    print(i)
    """)
    print("outputs:")
    for i in range(5):
        print(i)
    print("for loops with a step:")
    print("""
for i in range(0, 10, 2):
    print(i)
    """)
    print("outputs:")
    for i in range(0, 10, 2):
        print(i)
    print("for loops with a list:")
    print("""
for i in [1, 2, 3, 4, 5]:
    print(i)
    """)
    print("outputs:")
    for i in [1, 2, 3, 4, 5]:
        print(i)
    print("for loops with a dictionary:")
    print("""
for key, value in {'a': 1, 'b': 2, 'c': 3}.items():
    print(key, value)
    """)
    print("outputs:")
    for key, value in {'a': 1, 'b': 2, 'c': 3}.items():
        print(key, value)
    print("for loops with a string:")
    print("""
for letter in 'hello':
    print(letter)
    """)
    print("outputs:")
    for letter in 'hello':
        print(letter)
    print("break and continue:")
    print("""
for i in range(10):
    if i == 5:
        break
    print(i)
    """)
    print("outputs:")
    for i in range(10):
        if i == 5:
            break
        print(i)
    print("""
for i in range(10):
    if i == 5:
        continue
    print(i)
    """)
    print("outputs:")
    for i in range(10):
        if i == 5:
            continue
        print(i)


def functions():
    print("functions() called")
    print("functions are used to group code.")
    print("functions are defined using the def keyword.")
    print("functions can take arguments.")
    print("functions can return values.")
    print("functions can be called.")
    print("""
def add(x, y):
    return x + y
    """)
    print("outputs:")
    def add_1(x, y):
        return x + y
    print("add(5, 10) is", add_1(5, 10))
    print("functions can have default arguments.")
    print("""
def greet(name='John'):
    return 'Hello, ' + name + '!'
    """)
    print("outputs:")
    def greet(name='John'):
        return 'Hello, ' + name + '!'
    print("greet() is", greet())
    print("greet('Alice') is", greet('Alice'))
    print("functions can have variable arguments.")
    print("""
def add(*args):
    return sum(args)
    """)
    print("outputs:")
    def add_2(*args):
        return sum(args)
    print("add(1, 2, 3, 4, 5) is", add_2(1, 2, 3, 4, 5))
    print("functions can have keyword arguments.")
    print("""
def person(**kwargs):
    return kwargs
    """)
    print("outputs:")
    def person(**kwargs):
        return kwargs
    print("person(name='John', age=25) is", person(name='John', age=25))
    print("functions can return multiple values.")
    print("""
def add_sub(x, y):
    return x + y, x - y
    """)
    print("outputs:")
    def add_sub(x, y):
        return x + y, x - y
    print("add_sub(5, 10) is", add_sub(5, 10))
    print("functions can be used as arguments.")
    print("""
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def calc(x, y, op):
    return op(x, y)
    """)
    print("outputs:")
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def calc(x, y, op):
        return op(x, y)
    print("calc(5, 10, add) is", calc(5, 10, add))
    print("calc(5, 10, sub) is", calc(5, 10, sub))


def lists():
    print("lists() called")
    print("lists are used to store multiple values.")
    print("lists are created using square brackets.")
    print("lists can contain any type of value.")
    print("lists can be accessed using an index.")
    print("lists can be sliced using a start and end index.")
    print("lists can be modified using an index.")
    print("lists can be modified using a slice.")
    print("list_1 = [1, 2, 3, 4, 5]")
    list_1 = [1, 2, 3, 4, 5]
    for i in range(len(list_1)):
        print("list_1[{}] is".format(i), list_1[i])
    print("list_1[0:3] is", list_1[0:3])
    list_1[0] = 10
    print("list_1[0] = 10")
    print("list_1 is", list_1)
    list_1[0:3] = [1, 2, 3]
    print("list_1[0:3] = [1, 2, 3]")
    print("list_1 is", list_1)
    print("lists can be modified using methods.")
    print("list_1.append(6)")
    list_1.append(6)
    print("list_1 is", list_1)
    print("list_1.insert(0, 0)")
    list_1.insert(0, 0)
    print("list_1 is", list_1)
    print("list_1.pop()")
    list_1.pop()
    print("list_1 is", list_1)
    print("list_1.remove(3)")
    list_1.remove(3)
    print("list_1 is", list_1)
    print("list_1.reverse()")
    list_1.reverse()
    print("list_1 is", list_1)
    print("list_1.sort()")
    list_1.sort()
    print("list_1 is", list_1)
    print("list are reference type")
    print("list_2 = list_1")
    list_2 = list_1
    print("list_1 is", list_1)
    print("list_2 is", list_2)
    print("list_1[0] = 100")
    list_1[0] = 100
    print("list_1 is", list_1)
    print("list_2 is", list_2)
    print("list_1 and list_2 are the same list.")
    print("to create a copy of a list use the copy method.")
    print("list_2 = list_1.copy()")
    list_2 = list_1.copy()
    print("list_1 is", list_1)
    print("list_2 is", list_2)
    print("list_1[0] = 1000")
    list_1[0] = 1000
    print("list_1 is", list_1)
    print("list_2 is", list_2)

def dictionaries():
    print("dictionaries() called")
    print("dictionaries are used to store key value pairs.")
    print("dictionaries are created using curly brackets.")
    print("dictionaries can contain any type of key and value.")
    print("dictionaries can be accessed using a key.")
    print("dictionaries can be modified using a key.")
    print("dictionaries can be modified using methods.")
    print("person = {'name': 'John', 'age': 25}")
    person = {'name': 'John', 'age': 25}
    print("person['name'] is", person['name'])
    person['name'] = 'Alice'
    print("person['name'] = 'Alice'")
    print("person is", person)
    print("perosn = {'name': 'Alice', 'age': 25}")
    print("person['name'] is", person['name'])
    print("person['age'] is", person['age'])
    print("person.keys() is", person.keys())
    print("person.values() is", person.values())
    print("person.items() is", person.items())
    print("person.pop('age')")
    person.pop('age')
    print("person is", person)
    print("person.clear()")
    person.clear()
    print("person is", person)
    print("dictionaries are reference type.")
    print("person_2 = person")
    person_2 = person
    print("person is", person)
    print("person_2 is", person_2)
    print("person['name'] = 'Alice'")
    person['name'] = 'Alice'
    print("person is", person)
    print("person_2 is", person_2)
    print("person and person_2 are the same dictionary.")
    print("to create a copy of a dictionary use the copy method.")
    print("person_2 = person.copy()")
    person_2 = person.copy()
    print("person is", person)
    print("person_2 is", person_2)

print("""
1. variables
2. if statements
3. loops
4. functions
5. lists
6. dictionaries
""")
choice = input("Enter choice: ")
match choice:
    case "1":
        variables()
    case "2":
        if_statements()
    case "3":
        loops()
    case "4":
        functions()
    case "5":
        lists()
    case "6":
        dictionaries()
    case _:
        warn("Invalid choice")
