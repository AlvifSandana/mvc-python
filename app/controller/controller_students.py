from jinja2 import Template
from ..model.model_students import ModelStudents


class ControllerStudents:
    def index(self):
        try:
            mdl = ModelStudents()
            data = mdl.read_all()
            html = ""
            for d in data:
                html += f"<tr><td>{d['nim']}</td><td>{d['nama']}</td><td>{d['angkatan']}</td></tr>"
            with open('app/view/liststudents.html', 'r') as h:
                tmp = h.read()
            templat_html = Template(tmp)
            rendered = templat_html.render(listmhs=html)
            return rendered
        except Exception as e:
            print(e)

    def pageaddstudent(self):
        try:
            with open('app/view/addnewstudent.html', 'r') as rf:
                tmp = rf.read()
            template = Template(tmp)
            rendered = template.render()
            return rendered
        except Exception as e:
            print(e)

    def addstudent(self, postdata):
        try:
            mdl = ModelStudents()
            mdl.create(postdata)
        except Exception as e:
            print(e)
