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
        else:
            engine.symbols.append(Symbol({'x': line_number, 'y': i}))
            recording = False

with open('./input.txt', 'r') as file:
    input_lines = file.readlines()

engine = Engine()
for line_number, line in enumerate(input_lines):
    parse_manual_line(engine, line.strip(), line_number)

output = sum(n.value for n in engine.nums if any(
    (s.position['y'] >= (n.position['y'] - 1)) and
    (s.position['y'] <= (n.position['y'] + n.num_of_digits)) and
    (abs(s.position['x'] - n.position['x']) <= 1)
    for s in engine.symbols
))

print(output)
