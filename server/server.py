import socket
import os
import pathlib
import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os


def start_server(host_ip, port, shared_path):
    os.chdir(shared_path)
    Handler = http.server.SimpleHTTPRequestHandler

    link = "http://" + host_ip + ":" + str(port)

    url = pyqrcode.create(link)
    url.svg("share_qr.svg", scale=8)
    webbrowser.open('share_qr.svg')
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("serving at port", port)
        print("Type this in your Browser", link)
        print("or Use the QRCode")
        httpd.serve_forever()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IP = s.getsockname()[0]
    PORT = 8010

    drive = pathlib.Path.home().drive
    path = f"{drive}\\host\\shared_files"

    with open("../host_config", "w+") as f:
        f.write(f"{path}\n{IP}\n{PORT}")

    if not os.path.exists(path):
        print(f"Creating {path}.")
        os.makedirs(path)
    else:
        print("Shared folder already exists.")

    start_server(IP, PORT, path)


if __name__ == "__main__":
    main()
