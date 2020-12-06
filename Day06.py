# DATA
data = {}
with open("Data - Day06.txt") as file:
    num_group = 0
    for line in file:
        if len(line.strip()) == 0:
            num_group += 1
            continue
        else: 
          data.setdefault(num_group, []).append(line.strip())

# GOAL 1
"""
The form asks a series of 26 yes-or-no questions marked a through z. 
All you need to do is identify the questions for which anyone in your group answers "yes".

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
"""
def part1(data):
    cnt = 0
    for key in list(data.keys()):
        letters = set("".join(data[key]))
        cnt += len(letters)
    print(f"The sum equals {cnt}")

part1(data)

# GOAL 2
"""
You don't need to identify the questions to which anyone answered "yes"; 
you need to identify the questions to which everyone answered "yes"!

For each group, count the number of questions to which everyone answered "yes". 
What is the sum of those counts?
"""
def part2(data):
    alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
    cnt = 0
    for key in list(data.keys()):
        lst = data[key]
        for i in alphabet:
            let_cnt = 0
            for string in lst:
                if i in string:
                    let_cnt += 1
            if let_cnt == len(lst):
                cnt += 1

    print(f"Now the sum is only {cnt}")

part2(data)
        







