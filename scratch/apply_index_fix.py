with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Path replacement
old_path = '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>'
new_path = '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>'

assert old_path in c, "old_path not found in index.html"

# 2. Motion div replacement
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

assert old_motion in c, "old_motion not found in index.html"

c_updated = c.replace(old_path, new_path).replace(old_motion, new_motion)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c_updated)

print("index.html updated successfully!")
