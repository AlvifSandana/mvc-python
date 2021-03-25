from jinja2 import Template
from ..model.model_mhs import ModelMahasiswa


class ControllerMahasiswa:
    def index(self):
        try:
            mdl = ModelMahasiswa()
            data = mdl.read()
            html = ""
            for d in data:
                html += f"<tr><td>{d['nim']}</td><td>{d['nama']}</td><td>{d['angkatan']}</td></tr>"
            with open('app/view/listmhs.html', 'r') as h:
                tmp = h.read()
            templat_html = Template(tmp)
            rendered = templat_html.render(listmhs=html)
            return rendered
        except Exception as e:
            error = e
            print(error)
