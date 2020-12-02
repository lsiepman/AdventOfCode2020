import re
import pandas as pd 

# DATA
data = []
with open("Data - Day02.txt") as file:
    for line in file:
        data.append(line.strip())

# Goal 1
"""
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number 
of times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

How many passwords are valid according to their policies?
"""

# ANSWER 1
def convert_to_df(data):
    df = {"min_val": [], "max_val": [], "letter": [], "password": []}
    for i in data:
        df["min_val"].append(int(re.search(r"^[0-9]+", i).group()))
        df["max_val"].append(int(re.search(r"-([0-9]+)", i).group(1)))
        df["letter"].append(re.search(r"([a-z]):", i).group(1))
        df["password"].append(re.search(r"[a-z]+$", i).group())
    
    return pd.DataFrame(df)

def count_letter(df):
    num_times = []
    for idx in df.index:
        let = df["letter"][idx]
        pas = df["password"][idx]
        num_times.append(pas.count(let))

    df["occurrence"] = num_times
    
    return df

def check_valid(df):
    valid = []
    for idx in df.index:
        val = df["occurrence"][idx]
        min_val = df["min_val"][idx]
        max_val = df["max_val"][idx]

        valid.append(True if val >= min_val and val <= max_val else False) 
    
    df["valid"] = valid

    return df

def part_1(data):
    df = convert_to_df(data)
    df = count_letter(df)
    df = check_valid(df)
    print(f"There are {sum(df.valid)} valid passwords in the database")

part_1(data)

# Goal 2
"""
Each policy actually describes two positions in the password, 
where 1 means the first character, 2 means the second character, 
and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
"""
# ANSWER 2
def check_letter_location(df):
    valid = []
    for idx in df.index:
        pos1 = df["min_val"][idx]
        pos2 = df["max_val"][idx]
        pas = df["password"][idx]
        let0 = df["letter"][idx]

        let1 = pas[pos1 - 1]
        let2 = pas[pos2 - 1]

        if let1 == let2:
            valid.append(False)
        elif let1 == let0 or let2 == let0:
            valid.append(True)
        else:
            valid.append(False)
    
    df["valid"] = valid

    return df

def part_2(data):
    df = convert_to_df(data)
    df = check_letter_location(df)
    print(f"The database now has {sum(df.valid)} valid passwords")

part_2(data)