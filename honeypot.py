import socket
import threading
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='honeypot.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Honeypot Configuration
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 2222       # Port for the fake SSH service

def handle_client(client_socket, address):
    logging.info(f"Connection attempt from {address[0]}:{address[1]}")
    welcome_message = "SSH-2.0-OpenSSH_7.4\r\n"
    client_socket.send(welcome_message.encode())

    try:
        data = client_socket.recv(1024).decode()
        if data:
            logging.info(f"Data received from {address[0]}: {data.strip()}")
    except Exception as e:
        logging.error(f"Error handling client {address[0]}: {e}")
    finally:
        client_socket.close()

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    logging.info(f"Honeypot listening on {HOST}:{PORT}...")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    try:
        start_honeypot()
    except KeyboardInterrupt:
        logging.info("Honeypot shutting down...")
