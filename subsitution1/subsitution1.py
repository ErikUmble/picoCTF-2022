#from string import upper, lower
char_map = {"m" : "p",
            "k" : "i",
            "w": "c",
            "r": "o",
            "y" : "t",
            "h" : "f",
            "i" : "a",
            "a" : "r",
            "l" : "n",
            "z" : "h",
            "s" : "e",
            "v" : "l",
            "j" : "g",
            "g" : "s",
            "b" : "u",
            "u" : "y",
            "o" : "m",
            "d" : "w",
            "x" : "v",
            "n" : "d",
            "q" : "b",
            "c" : "k",
            "f" : "q"}
print(len(char_map))
decr = ""
with open("message.txt", "r") as file:
    for l in file.read():
        if not l.isalpha():
            decr += l
            continue
        if l.isupper():
            decr += char_map.get(l.lower(), l).upper()
            continue
        else:
            decr += char_map.get(l, l)

print(decr)

decr = ""
for l in "mkwrWYH{HA4FB3LWU_4774WC5_4A3_W001_7II384QW}":
    if not l.isalpha():
        decr += l
        continue
    if l.isupper():
        decr += char_map.get(l.lower(), "-").upper()
        continue
    else:
        decr += char_map.get(l, "-")
print(decr)

