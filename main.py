import socket

host = input("Enter hostname: ") #example google.com etc
ports = [80, 443, 22, 8080] #add more ports if need

for port in ports:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1) 
    scan = sock.connect_ex((host,port))
    if scan == 0:
        print(f"{port}-> OPEN")
    else:
        print(f"{port}->{scan} ")

        
sock.close()
