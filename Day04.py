# IMPORTS
import re

# DATA
data = {}
with open("Data - Day04.txt") as file:
    num_passport = 0
    for line in file:
        if len(line.strip()) == 0:
            data[num_passport] = " ".join(data[num_passport])
            num_passport += 1
            continue
        else: 
          data.setdefault(num_passport, []).append(line.strip())
    data[len(data.keys()) - 1] = " ".join(data[len(data.keys()) - 1])

# GOAL 1
"""
Count the number of valid passports - those that have all required fields. 
Treat cid as optional. In your batch file, how many passports are valid?
Required fields are: 
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID) [optional]
"""
def part1(req_fields, data):
    valid = 0
    for idx in list(data.keys()):
        string = data[idx]
        val = 0
        for i in req_fields:
            if re.search(f"{i}", string):
                val += 1
        if val == len(req_fields):
            valid += 1   
    
    return valid

print(f'There are {part1(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"], data)} valid passports')

# GOAL 2
"""
You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

"""
def select_valid(req_fields, data):
    new_data = {}
    for idx in list(data.keys()):
        string = data[idx]
        val = 0
        for i in req_fields:
            if re.search(f"{i}", string):
                val += 1
        if val == len(req_fields):
            new_data[idx] = string
    
    return new_data

def validate_general(regex, string):
    if re.search(regex, string):
        return True
    else:
        return False

def validate_year(field, min_year, max_year, string):
    regex = f"{field}" + r":([0-9]{4})"
    year = int(re.search(regex, string).group(1))
    if min_year <= year <= max_year:
        return True
    else:
        return False

def validate_height(string):
    if "cm" not in string and "in" not in string:
        return False
    val = re.search(r"hgt:([0-9]+[cmin]+)", string).group(1)
    h = int(val[:-2])
    if "cm" in val and 150 <= h <= 193:
        return True
    elif "in" in val and 59 <= h <= 76:
        return True
    else:
        return False

def part2(req_fields, data):
    candidate = select_valid(req_fields, data) 
    valid = 0
    
    for idx in list(candidate.keys()):
        val = 0
        string = candidate[idx]
        if validate_year("byr", 1920, 2002, string):
            val += 1
        
        if validate_year("iyr", 2010, 2020, string):
            val += 1

        if validate_year("eyr", 2020, 2030, string):
            val += 1

        if validate_height(string):
            val += 1

        if validate_general(r"#[0-9a-f]{6}", string):
            val += 1

        if validate_general(r"ecl:(amb|blu|brn|gry|grn|hzl|oth){1}", string):
            val += 1

        if validate_general(r"pid:[0-9]{9}(?!\S)", string):
            val += 1

        if val == len(req_fields):
            valid += 1   

    return valid

print(f'There are {part2(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"], data)} valid passports remaining')
