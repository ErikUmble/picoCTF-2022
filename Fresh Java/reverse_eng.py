
pos_map = {}
with open("Decompiled.txt", "r") as file:
    for line in file:
        if "else if" in line:
            position = int(line.split("(")[2].split(")")[0])
            char = line.split("'")[1].split("'")[0]
            pos_map[position] = char

flag = ''.join([pos_map[pos] for pos in range(34)])
print(flag)
