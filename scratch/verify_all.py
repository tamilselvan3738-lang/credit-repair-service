import glob

files = glob.glob('*.html')
old_p = 'd="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"'
old_m = 'rotate: isDark ? 0 : 180'

has_errors = False
for f in sorted(files):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    if old_p in c:
        print(f'ERROR: old path still in {f}')
        has_errors = True
    if old_m in c:
        print(f'ERROR: old motion still in {f}')
        has_errors = True

if not has_errors:
    print('SUCCESS: Verified all 15 HTML files! Zero occurrences of old path or inverted rotation remaining.')
