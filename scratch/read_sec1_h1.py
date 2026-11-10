with open("home-2.html", "r", encoding="utf-8") as f:
    c = f.read()

pos = c.find('home2-hero-executive-wealth')
print(c[max(0, pos-5000):max(0, pos-3500)])
