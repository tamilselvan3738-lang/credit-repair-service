import glob

# The 9 navbar files that have the motion.div animation
nav_files = [
    'about.html', 'contact.html', 'credit-repair.html', 'home-2.html',
    'navbar.html', 'plans.html', 'resources.html', 'services.html'
]

old_path = '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>'
new_path = '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>'

old_motion = """<motion.div
                    initial={false}
                    animate={{ rotate: isDark ? 0 : 180, scale: isDark ? 1 : 0.9 }}
                    transition={{ duration: 0.35, ease: "easeInOut" }}
                  >
                    {isDark ? (
                      <IconSun className="w-4 h-4 text-amber-400 group-hover:rotate-45 transition-transform" />
                    ) : (
                      <IconMoon className="w-4 h-4 text-indigo-600 group-hover:-rotate-12 transition-transform" />
                    )}
                  </motion.div>"""

new_motion = """<motion.div
                    key={isDark ? "dark" : "light"}
                    initial={{ rotate: -30, opacity: 0, scale: 0.8 }}
                    animate={{ rotate: 0, opacity: 1, scale: 1 }}
                    transition={{ duration: 0.22, ease: "easeOut" }}
                  >
                    {isDark ? (
                      <IconSun className="w-4 h-4 text-amber-400 group-hover:rotate-45 transition-transform" />
                    ) : (
                      <IconMoon className="w-4 h-4 text-indigo-600 group-hover:-rotate-12 transition-transform" />
                    )}
                  </motion.div>"""

for fn in nav_files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    
    assert old_path in c, f"old_path not found in {fn}"
    assert old_motion in c, f"old_motion not found in {fn}"
    
    c = c.replace(old_path, new_path)
    c = c.replace(old_motion, new_motion)
    
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated {fn}")

# Other standalone pages: 404, login, registration, registeration
standalone_files = ['404.html', 'login.html', 'registration.html', 'registeration.html']
for fn in standalone_files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    assert old_path in c, f"old_path not found in {fn}"
    c = c.replace(old_path, new_path)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated {fn}")

# Dashboards: admin-dashboard.html, user-dashboard.html
dash_files = ['admin-dashboard.html', 'user-dashboard.html']
for fn in dash_files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    assert old_path in c, f"old_path not found in {fn}"
    c = c.replace(old_path, new_path)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated {fn}")

print("All files updated successfully!")
