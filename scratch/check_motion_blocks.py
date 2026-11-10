import glob, re

target_files = ['about.html', 'contact.html', 'credit-repair.html', 'home-2.html', 'index.html', 'navbar.html', 'plans.html', 'resources.html', 'services.html']

for fn in target_files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    
    pos = c.find('rotate: isDark ? 0 : 180')
    if pos != -1:
        start = c.rfind('<motion.div', 0, pos)
        end = c.find('</motion.div>', pos) + len('</motion.div>')
        print(f"=== {fn} ===")
        print(c[start:end])
        print("---")
