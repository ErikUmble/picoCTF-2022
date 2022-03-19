#from string import upper, lower
char_map = {"f":"p",
            "s":"i",
            "t":"c",
            "w":"o",
            "t":"c",
            "x":"t",
            "a":"f",
            "u":"m",
            "d":"e",
            "p":"n",
            "g":"s",
            "b":"u",
            "c":"r",
            "r":"d",
            "j":"a",
            "v":"l",
            "l":"y"}
print(len(char_map))
decr = ""
with open("message.txt", "r") as file:
    for l in file.read():
        if not l.isalpha():
            decr += l
            continue
        if l.isupper():
            decr += char_map.get(l.lower(), '-').upper()
            continue
        else:
            decr += char_map.get(l, '-')

with open("decoded.txt", "w") as file, open("message.txt", "r") as m:
    mes = m.read()
    file.writelines([mes,"\n", decr])
    print(mes)
    print(decr)

decr = ""
for l in "fstwTXA{P6C4U_4P41L515_15_73R10B5_702A03AT}":
    if not l.isalpha():
        decr += l
        continue
    if l.isupper():
        decr += char_map.get(l.lower(), "-").upper()
        continue
    else:
        decr += char_map.get(l, "-")
print(decr)

