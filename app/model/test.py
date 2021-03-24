import json
from jinja2 import Template

html = ""
with open('../../db/data.json') as f:
    data = json.load(f)

for d in data['mahasiswa']:
    html += f"<tr><td>{d['nim']}</td><td>{d['nama']}</td><td>{d['angkatan']}</td></tr>"
templat = Template(html)
templat.render()

print(data)
