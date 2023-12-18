import math
import re

input_file = "Input\day8.txt"

# To match the format of input files for the Basilisk.
q = {8: open(input_file).read().strip()}

instructions = q[8].split("\n")[0]
nodes = [re.findall(r"(\w+) = \((\w+), (\w+)\)", line) for line in q[8].split("\n")[2:]]
first_nodes = [n[0][0] for n in nodes if n[0][0].endswith("A")]
nodes = {n[0][0]: n[0][1:] for n in nodes}


all_steps = []
for node in first_nodes:
    cur = node
    steps = 0
    while not cur.endswith("Z"):
        for d in instructions:
            steps += 1
            if d == "R":
                cur = nodes[cur][1]
            elif d == "L":
                cur = nodes[cur][0]
    all_steps.append(steps)

# 13524038372771
print("Day 08 Part 2:", math.lcm(*all_steps))
