"""
Modul server.py
23 Marent 2021
by Alvif Sandana Mahardika
"""
import socket
import time

from app.controller.controller_about import ControllerAbout
from app.controller.controller_students import ControllerStudents
from app.controller.controller_dashboard import ControllerDashboard


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
            # Waiting for client connection
            client_connection, client_address = self.server_socket.accept()

            # get request from client
            request = client_connection.recv(1024).decode()
            print(request)

            # splitting request string for routes handling
            path = request.split(' ')

            # instantiate controller object
            dashboard = ControllerDashboard()
            about = ControllerAbout()
            student = ControllerStudents()

            # handling routes
            if path[1] == '/':
                # send HTTP response
                response = f"HTTP/1.0 200 OK\n\n{dashboard.index()}"
            elif path[1] == '/about':
                # send HTTP response
                response = f"HTTP/1.0 200 OK\n\n{about.index()}"
            elif path[1] == '/mahasiswa':
                # send HTTP response
                response = f"HTTP/1.0 200 OK\n\n{student.index()}"
            elif path[0] == 'GET' and path[1] == '/mahasiswa/add':
                # send HTTP response
                response = f"HTTP/1.0 200 OK\n\n{student.pageaddstudent('')}"
            elif path[0] == 'POST' and path[1] == '/mahasiswa/add':
                # send HTTP response
                response = f"HTTP/1.0 200 OK\n\n{student.index()}"
                print(path[len(path) - 1])
            else:
                with open('app/view/404.html', 'r') as nf:
                    html_ren = nf.read()
                response = f"HTTP/1.0 404 Not Found\n\n{html_ren}"

            # send response to client
            client_connection.sendall(response.encode())
            client_connection.close()


    def serve_end(self):
        # close socket
        self.server_socket.close()
