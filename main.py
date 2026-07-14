import socket
import time

host = input("Enter hostname: ")
ports = [80, 443, 22, 8080] #add more ports if need
open_ports=0
start = time.perf_counter()
ip=socket.gethostbyname(host)
print(f"IP: {ip}")
for port in ports:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1) 
    services = socket.getservbyport(port)
    #print(services)
    

    scan = sock.connect_ex((host,port))
    if scan == 0:
        print(f"{port}({services}) -> OPEN")
        open_ports = open_ports+1 #or just do open_ports+=1
    else:
        print(f"{port}({services}) -> CLOSED ")

    sock.close()

end = time.perf_counter()
took = end-start
if took<1:
    print(f"\nFound {open_ports} open ports in {took*1000:.0f}ms")
else:
    print(f"\nFound {open_ports} open ports in {took:.1f}s")
