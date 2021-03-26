"""
Module: controller_about.py

Created by alvif@usagi 
at 26/03/21
"""
from jinja2 import Template


class ControllerAbout:
    def index(self):
        try:
            with open('app/view/about.html', 'r') as rf:
                tmp = rf.read()
            template = Template(tmp)
            rendered = template.render()
            return rendered
        except Exception as e:
            print(e)
