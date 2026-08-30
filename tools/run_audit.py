from pathlib import Path
import re

src = Path('tools/audit_optimize.py').read_text(encoding='utf-8')
# The CSV anchor differs only in quoting across Python/JS; apply it separately below.
filtered = '\n'.join(line for line in src.splitlines() if "'safe csv')" not in line)
ns = {'__name__': '__main__'}
exec(compile(filtered, 'tools/audit_optimize.py', 'exec'), ns)

p = Path('index.html')
s = p.read_text(encoding='utf-8')
pattern = r"function csvEscape\(v=''\)\{return `\"\$\{String\(v\)\.replaceAll\('\"','\"\"'\)\}\"`\}"
m = re.search(pattern, s)
if not m:
    raise SystemExit('csvEscape anchor not found')
replacement = "function csvEscape(v=''){let x=String(v);if(/^[=+\\-@]/.test(x))x=\"'\"+x;return `\"${x.replaceAll('\\\"','\\\"\\\"')}\"`}\nfunction downloadBlob(blob,name){const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=name;a.style.display='none';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1500)}"
s = s[:m.start()] + replacement + s[m.end():]
p.write_text(s, encoding='utf-8')

scripts = re.findall(r'<script>(.*?)</script>', s, re.S)
if len(scripts) != 1:
    raise SystemExit(f'expected one inline script after final patch, got {len(scripts)}')
Path('/tmp/app.js').write_text(scripts[0], encoding='utf-8')
print('Final audit patch complete; bytes:', len(s.encode('utf-8')))
