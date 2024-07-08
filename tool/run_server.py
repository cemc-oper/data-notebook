import socket
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler


def get_ip() -> str:
    """
    get ip address

    References
    -----------
    https://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-from-a-nic-network-interface-controller-in-python

    Returns
    -------
    str
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_port():
    """
    get an available port.

    References
    ----------
    https://stackoverflow.com/questions/1365265/on-localhost-how-do-i-pick-a-free-port-number

    Returns
    -------
    int
    """
    sock = socket.socket()
    sock.bind(('', 0))
    return sock.getsockname()[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("web_base")
    args = parser.parse_args()
    print(args.web_base)

    host = get_ip()
    port = get_port()

    print("Starting http server...")
    print(f"Please visit http://{host}:{port}")

    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
