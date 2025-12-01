position = 50
count_zeros = 0

rotation_list = []

with open("input.txt") as file:
    for line in file:
        clean = line.strip("\n")
        direction = clean[0]
        numerical_value = clean[1:]
        iteration_dict = {}
        iteration_dict["Direction:"] = direction
        iteration_dict["Value:"] = int(numerical_value)
        rotation_list.append(iteration_dict)

for entry in rotation_list:
    direction = entry["Direction:"]
    value = entry["Value:"]
    if direction == "L":
        position -= value
        while position < 0:
            position = position + 100
    elif direction == "R":
        position += value
        while position > 99:
            position = position - 100
    if position == 0:
        count_zeros += 1

print(count_zeros)
