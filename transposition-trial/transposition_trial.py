decr = ""
with open("message.txt", "r") as file:
    l = file.read().strip()
    for i in range(0, len(l), 3):
        substr = l[i+2] + l[i] + l[i+1]
        decr += substr

print(decr)
