"""
Module: controller_dashboard.py

Created by alvif
at 25/03/21
"""
from jinja2 import Template

class ControllerDashboard:
    def index(self):
        try:
            html = '<!DOCTYPE html>' \
                   '<html lang="en">' \
                   '<head>' \
                   '<meta charset="UTF-8">' \
                   '<title>Dashboard</title>' \
                   '</head>' \
                   '<body>' \
                   '<center>' \
                   '<h1>Dashboard</h1>' \
                   '</center>' \
                   '</body>' \
                   '</html>'
            with open('app/view/index.html', 'w') as f:
                f.write(html)
            with open('app/view/index.html', 'r') as rf:
                tmp = rf.read()
            template = Template(tmp)
            rendered = template.render()
            return rendered
        except Exception as e:
            print(e)
