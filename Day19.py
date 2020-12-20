import re

rules = {}
inp = []
with open("Data - Day19.txt") as file:
    for line in file:
        line = line.strip()
        if re.match(r"\d", line):
            key = re.search(r"^[0-9]+", line).group()
            vals = re.search(r"[0-9a-z\"|\s]+$", line).group()
            vals = vals.strip().replace('"', "")
            rules[key] = f"( {vals} )"

        elif re.match(r"[ab]+", line):
            inp.append(line)

# GOAL 1
"""Your goal is to determine the number of messages that completely match rule 0. """

# which rules contain the a and b

def has_digit(string):
    return bool(re.search(r'\d', string))

def find_key(rules, exclusion):
    to_check = [x for x in rules if x not in exclusion]
    for i in to_check:
        rexp = has_digit(rules[i])
        if not rexp:
            return i
    return False

def replace_found(rules, key):
    for i in rules:

        regex = r"\s(" + key + r")\s"
        rexp = re.search(regex, rules[i])

        for _ in range(4):
            if rexp:
                rules[i] = re.sub(regex, f" {rules[key]} ", rules[i])
        

def clean_rules(rules):
    for key in rules:
        rules[key] = re.sub(r"\s", "", rules[key])

exclusion = []
while has_digit(rules["0"]):
    key = find_key(rules, exclusion)
    exclusion.append(key)
    replace_found(rules, key)

clean_rules(rules)

regex = r"^" + rules["0"] + r"$"
cnt = 0
for i in inp:
    if re.match(regex, i):
        cnt += 1

print(f"Part 1 matches {cnt} messages")

# GOAL 2
"""As you look over the list of messages, 
you realize your matching rules aren't quite right. 
To fix them, completely replace rules 8: 42 and 11: 42 31 with the following:

8: 42 | 42 8
11: 42 31 | 42 11 31
(and 0: 8 11)
"""

cnt = 0
for n in range(1, 10):
    match_this = f"^({rules['42']}+{rules['42']}{{{n}}}{rules['31']}{{{n}}})$"
    for i in inp:
        if re.search(match_this, i):
            cnt += 1

print(f"Part 2 matches {cnt} message") 