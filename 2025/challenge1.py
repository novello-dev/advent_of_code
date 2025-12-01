position = 50
zero_count = 0

rotations = []

with open("challenge1_input.txt") as file:
    for line in file:
        direction = line[0]
        numerical_value = line[1:]
        move = {}
        move["direction"] = direction
        move["value"] = int(numerical_value)
        rotations.append(move)

for entry in rotations:
    direction = entry["direction"]
    value = entry["value"]
    if direction == "L":
        position -= value
        while position < 0:
            position = position + 100
    elif direction == "R":
        position += value
        while position > 99:
            position = position - 100
    if position == 0:
        zero_count += 1

print(zero_count)
