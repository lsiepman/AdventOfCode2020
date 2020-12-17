import re
import itertools
from functools import reduce
from operator import mul
import pandas as pd

# DATA
other_tickets = []
rules = {}
my_ticket = []
with open("Data - Day16.txt") as file:
    oth_marker = False
    rule_marker = True
    my_maker = False
    for line in file:
        if oth_marker:
            other_tickets.append(line.strip().split(","))
        elif "nearby tickets" in line:
            oth_marker = True
        elif line == "\n":
            rule_marker = False
            my_maker = False
        elif rule_marker:
            r = re.search(r"(^[ a-z]+): ([a-z-0-9 ]+)", line)
            k = r.group(1)
            v = r.group(2)
            rules[k] = v
        elif my_maker:
            my_ticket.extend(line.strip().split(","))
        elif "your ticket" in line:
            my_maker = True
        

# GOAL 1
"""
The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field.
Adding together all of the invalid values produces your ticket scanning error rate.
"""
valid_ranges = {"valid_from": [], "valid_to": [], "category": []}

for i in rules:
    rule = re.findall(r"[0-9]+", rules[i])
    rule = [int(j) for j in rule]
    valid_ranges["valid_from"].extend([rule[0], rule[2]])
    valid_ranges["valid_to"].extend([rule[1], rule[3]])
    valid_ranges["category"].extend([i, i])

valid_ranges = pd.DataFrame(valid_ranges)


def check_valid(valid, tickets):
    invalid = []

    for ticket in tickets:
        for num in ticket:
            num = int(num)
            between = False
            for idx in valid.index:
                if valid["valid_from"][idx] <= num <= valid["valid_to"][idx]:
                    between = True
                    break
            if not between:
                invalid.append(num)

    return sum(invalid)

print(f"The ticket scanning error rate equals: {check_valid(valid_ranges, other_tickets)} for part 1")

# GOAL 2
"""
Now that you've identified which tickets contain invalid values, discard those tickets entirely. 
Use the remaining valid tickets to determine which field is which.

Once you work out which field is which, 
look for the six fields on your ticket that start with the word departure. 
What do you get if you multiply those six values together?
"""
def only_valid(valid, tickets):
    invalid = []
    for ticket in tickets:
        for num in ticket:
            num = int(num)
            between = False
            for idx in valid.index:
                if valid["valid_from"][idx] <= num <= valid["valid_to"][idx]:
                    between = True
                    break
            if not between:
                invalid.append(ticket)

    valid_tickets = [i for i in tickets if i not in invalid]
    
    return valid_tickets

def create_from_to_except(valid_ranges):
    new_df = {"cat": [], "fro": [], "to": [], "ex_fro": [], "ex_to": []}
    
    uni_cats = valid_ranges["category"].unique()
    for i in uni_cats:
        temp = valid_ranges[valid_ranges["category"] == i].reset_index(drop=True)

        new_df["cat"].append(i)
        new_df["fro"].append(temp["valid_from"][0])
        new_df["to"].append(temp["valid_to"][1])
        new_df["ex_fro"].append(temp["valid_to"][0])
        new_df["ex_to"].append(temp["valid_from"][1])

    return pd.DataFrame(new_df)

def check_category(rule_row, tickets, ticket_values):
    for tic in tickets:
        for idx in ticket_values:
            if (
                rule_row["fro"] <= int(tic[idx]) <= rule_row["to"] and not 
                rule_row["ex_fro"] < int(tic[idx]) < rule_row["ex_to"]
                ):
                pass
            else:
                ticket_values[idx].remove(rule_row["cat"])

    return ticket_values

def find_idx_cat(ticket_values):
    final = []
    rem = "placeholder"
    while len(ticket_values) > 0:
        for i in ticket_values:
            if len(ticket_values[i]) == 1:
                final.append((i, ticket_values[i][0]))
                rem = ticket_values[i][0]
                del ticket_values[i]
                break

        for i in ticket_values:
            if rem in ticket_values[i]:
                ticket_values[i].remove(rem)
        
    return final

def prod(iterable): # default function in the math module in python 3.9
    return reduce(mul, iterable, 1)

df_ranges = create_from_to_except(valid_ranges)
tickets = only_valid(valid_ranges, other_tickets)
tickets.append(my_ticket)

ticket_values = {}
for i in range(len(my_ticket)):
    ticket_values[i] = list(rules.keys())

for row in df_ranges.index:
    ticket_values = check_category(df_ranges.iloc[row], tickets, ticket_values)

comb = find_idx_cat(ticket_values)

indices = [i for i,j in comb if "departure" in j]

print(f"The multiplication answer is {prod([int(j) for i,j in enumerate(my_ticket) if i in indices])}")