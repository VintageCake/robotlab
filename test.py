import socket

server = "127.0.0.1"
port = 50001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server,port))
    msg = s.recv(1024)
    print (f"Got this:  {msg!r}")
    s.sendall(b"Hello!")
    msg = s.recv(1024)
    print (f"Got this reply:  {msg!r}")
