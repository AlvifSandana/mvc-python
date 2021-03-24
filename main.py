"""
Modul main.py
23 Maret 2021
by Alvif Sandana Mahardika
"""
import time
from server import MyServer


# Menyiapkan host dan port
HOST = '127.0.0.1'
PORT = 8000

if __name__ == '__main__':
    httpd = MyServer(HOST, PORT)
    try:
        httpd.serve()
    except Exception as e:
        print(f'[{time.asctime()}] - Error occured!! {e}')
        print(f'[{time.asctime()}] - try to re-activate server...')
        time.sleep(5)
        httpd.serve()
    except KeyboardInterrupt as stop:
        print(f'[{time.asctime()}] - Server stopped ({stop}).')
        httpd.serve_end()
