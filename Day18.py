import re

# DATA
with open("Data - Day18.txt") as file:
    data = file.readlines()

data = [i.strip() for i in data]
test = "1 + (2 * 3) + (4 * (5 + 6))"
test2 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
# GOAL 1
"""
The homework (your puzzle input) consists of a series of expressions that consist of 
addition (+), multiplication (*), and parentheses ((...)). 
Just like normal math, parentheses indicate that the expression inside must be evaluated before 
it can be used by the surrounding expression. Addition still finds the sum of the 
numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, 
the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.
"""
def solve_parens(equation):
    while True:
        if "(" not in equation:
            break
        nums = re.search(r"\(([0-9\s*+]+)\)", equation)
        if nums:
            val = left_to_right(nums.group(1))
            equation = equation.replace(nums.group(), str(val))

    return equation



def left_to_right(equation):
    equation = equation.split(" ")
    result = 0
    next_operation = "+"
    for char in equation:
        if re.match(r"[0-9]+", char):
            val = int(char)
            if next_operation == "+":
                result += val
            elif next_operation == "*":
                result *= val
        elif re.match(r"[+*]", char):
            next_operation = char

    return result

def part1(data):
    values = []
    for eq in data:
        eq = solve_parens(eq)
        values.append(left_to_right(eq))
    return sum(values)

print(f"The part 1 sum of the entire input equals {part1(data)}")

# GOAL 2
"""
Now, addition and multiplication have different precedence levels, 
but they're not the ones you're familiar with. 
Instead, addition is evaluated before multiplication.

What do you get if you add up the results of evaluating the homework problems using these new rules?
"""
def calc_plus(equation):
    while True:
        if re.search(r"\([0-9]+\)", equation):
            val1 = re.search(r"\([0-9]+\)", equation).group()
            val2 = val1.replace("(", "").replace(")", "")
            equation = equation.replace(val1, val2)

        if re.search(r"(\s)?[0-9]+ \+ [0-9]+(\s)?", equation):
            plus = re.search(r"[0-9]+ \+ [0-9]+", equation).group()
            equation = equation.replace(plus, f"{eval(plus)}")
        elif "+" in equation and re.search(r"\(([0-9]+ \* [0-9]+)\)", equation):
            times = re.search(r"\(([0-9]+ \* [0-9]+)\)", equation).group(1)
            equation = equation.replace(f"({times})", f"({eval(times)})")
        elif "+" in equation and re.search(r"\(([0-9]+ \* [0-9]+ \* [0-9]+)\)", equation):
            times = re.search(r"\(([0-9]+ \* [0-9]+ \* [0-9]+)\)", equation).group()
            equation = equation.replace(f"{times}", f"{eval(times)}")
        elif "+" in equation and re.search(r"\(([0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+)\)", equation):
            times = re.search(r"\(([0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+)\)", equation).group()
            equation = equation.replace(f"{times}", f"{eval(times)}")
        elif "+" in equation and re.search(r"\([0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+\)", equation):
            times = re.search(r"\([0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+\)", equation).group()
            equation = equation.replace(f"{times}", f"{eval(times)}")
        elif "+" in equation and re.search(r"\([0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+\)", equation):
            times = re.search(r"\([0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+ \* [0-9]+\)", equation).group()
            equation = equation.replace(f"{times}", f"{eval(times)}")
        elif "+" not in equation:
            break
        else:
            print(equation)
            raise ValueError("Unexpected condition")
    return eval(equation)

def part2(data):
    results = []
    for eq in data:
        results.append(calc_plus(eq))
    return sum(results)

print(f"The new sum equals {part2(data)}")
