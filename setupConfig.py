al = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

with open("config.json", "w") as f:
    f.write("{\n\t\"list\": [[\"a\", \"a\"]")
    for x in range(26):
        for y in range(26):
            f.write(", [\"" + al[x] + "\", \"" + al[y] + "\"]")
    f.write("]\n}")
