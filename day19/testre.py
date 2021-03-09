import re

string = "abababcdecdecde"

p = re.compile("(ab)*(cde)*$")
print(p)
m = p.match(string)
print(m.group(0))
