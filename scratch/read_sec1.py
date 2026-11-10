with open("home-2.html", "r", encoding="utf-8") as f:
    c = f.read()

pos1 = c.find('<!-- SECTION 1:')
pos2 = c.find('<!-- SECTION 2:', pos1)
print(c[pos1:pos2])
