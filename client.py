import socket

SERVER_IP = '192.168.1.85'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.AF.STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    data = s.recv(1024)
    print(data)
    
input()
    