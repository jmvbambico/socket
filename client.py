import socket
import sys

STOP_COMMAND = "stop"
RESTART_COMMAND = "restart"
RUN_COMMAND = "run"

def connect_to_server(command, params=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(5)
    s.connect(("localhost", 2999))
    if params:
        command = command + " " + " ".join(params)

    byte_command = str.encode(command)
    s.sendall(byte_command)
    data = s.recv(1024)
    s.close()

    print(data.decode("utf-8"))

if len(sys.argv) >= 2:
    arg = sys.argv[1].lower()
else:
    arg = None

if arg in (STOP_COMMAND, RESTART_COMMAND, RUN_COMMAND):
    connect_to_server(arg, sys.argv[2:])
else:
    print("Use stop, restart, or run as argument")