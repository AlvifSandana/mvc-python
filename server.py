"""
Modul server.py
23 Marent 2021
by Alvif Sandana Mahardika
"""
import socket
import json
import time
from app.controller.controller_mhs import ControllerMahasiswa


class MyServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

    def serve(self):
        print(f'[{time.asctime()}] - Listening on port {self.port}')

        while True:
            # Menunggu koneksi dari client
            client_connection, client_address = self.server_socket.accept()

            # Mendapatkan request dari client
            request = client_connection.recv(1024).decode()
            print(request)

            path = request.split(' ')

            if path[1] == '/':
                # kirim HTTP response
                # memuat data.json
                fin = open('db/data.json')
                content = json.load(fin)
                fin.close()

                # menyiapkan vavriabel untuk file html
                html = ''

                # ambil data
                for d in content['mahasiswa']:
                    html += f"<tr><td>{d['nim']}</td><td>{d['nama']}</td><td>{d['angkatan']}</td></tr>"

                # gabung menjadi satu
                html_jadi = f'<html>' \
                            f'<head><title>JSON</title></head>' \
                            f'<body>' \
                            f'<table border="1"><tr><td>NIM</td><td>Nama</td><td>Angkatan</td></tr>{html}</table>' \
                            f'</body></html>'

                # tulis file html baru
                with open('app/view/index.html', 'w') as f:
                    f.write(html_jadi)

                with open('app/view/index.html', 'r') as h:
                    html_ren = h.read()

                # kirim HTTP response
                response = f"HTTP/1.0 200 OK\n\n{html_ren}"
            elif path[1] == '/about':
                with open('app/view/tentang.html', 'r') as h:
                    html_ren = h.read()

                # kirim HTTP response
                response = f"HTTP/1.0 200 OK\n\n{html_ren}"

            elif path[1] == '/mahasiswa':
                maha = ControllerMahasiswa()
                response = f"HTTP/1.0 200 OK\n\n{maha.index()}"
            else:
                with open('app/view/404.html', 'r') as nf:
                    html_ren = nf.read()

                response = f"HTTP/1.0 404 Not Found\n\n{html_ren}"

            # kirim respon ke client
            client_connection.sendall(response.encode())
            client_connection.close()


    def serve_end(self):
        # Menutup socket
        self.server_socket.close()
