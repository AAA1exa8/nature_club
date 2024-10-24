import math

class Number:
    def __init__(self, value, position, num_of_digits):
        self.value = value
        self.position = position
        self.num_of_digits = num_of_digits

class Symbol:
    def __init__(self, position):
        self.position = position

class Engine:
    def __init__(self):
        self.nums = []
        self.symbols = []

def is_numeric(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def parse_manual_line(engine, line, line_number):
    recording = False
    for i, char in enumerate(line):
        if char == '.':
            recording = False
            continue
        if is_numeric(char):
            if not recording:
                recording = True
                engine.nums.append(Number(int(char), {'x': line_number, 'y': i}, 1))
            else:
                engine.nums[-1].value = engine.nums[-1].value * 10 + int(char)
                engine.nums[-1].num_of_digits += 1
        elif char == '*':
            engine.symbols.append(Symbol({'x': line_number, 'y': i}))
            recording = False
        else:
            recording = False

with open('./input.txt', 'r') as file:
    input_lines = file.readlines()

engine = Engine()
for line_number, line in enumerate(input_lines):
    parse_manual_line(engine, line.strip(), line_number)

output = sum(
    math.prod(n.value for n in nums) for nums in [
        [n for n in engine.nums if 
            (g.position['y'] >= (n.position['y'] - 1)) and
            (g.position['y'] <= (n.position['y'] + n.num_of_digits)) and
            (abs(g.position['x'] - n.position['x']) < 2)
        ] for g in engine.symbols
    ] if len(nums) == 2
)

print(output)
