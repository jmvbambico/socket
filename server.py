import socket
import subprocess

STOP_COMMAND = "stop"
RESTART_COMMAND = "restart"
RUN_COMMAND = "run"
script_name = "script.sh"
host = "localhost"
port = 2999

s = None

def execute_script(data):
    params = data.split()[1:]
    print(f"Running {script_name} {params}")

    command = [script_name] + params
    output = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    output = output.stdout

    return output

def start():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()

    print(f'Server initialized on {host}:{port}...')

    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        data = data.decode("utf-8").strip()

        print('Client connected successfully: ', addr)

        if data in (STOP_COMMAND, RESTART_COMMAND):
            break
        elif data[:len(RUN_COMMAND)] == RUN_COMMAND:
            output = execute_script(data)
            conn.sendall(output)
        else:
            print("Received unknown command: " + data)

        conn.close()

    if data == STOP_COMMAND:
        stop()
    elif data == RESTART_COMMAND:
        restart()

def stop():
    print("Stopping...")

    if s:
        s.close()

def restart():
    print("Restarting...")
    stop()
    start()

if __name__ == "__main__":
    start()