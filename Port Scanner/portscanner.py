import sys
import time
import threading
import socket
import pyfiglet

print (pyfiglet.figlet_format("Port Scanner"))

start_time = time.time()

if (len(sys.argv) != 4 or sys.argv[1]=="" or sys.argv[2]=="" or sys.argv[3]==""):
    print ("Invalid argument ")
    print ( "USAGE: File name <HOST> <START PORT> <END PORT> ")
    sys.exit()


    

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

try: 
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print ("Name Resolution error")
    sys.exit()

print ("Port Scanning on: {}\n".format(target))

def scan_port (port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    value = s.connect_ex((target, port))
    if (not value):
        print ("Port {} is OPEN".format(port))
    s.close()    

# Create threads for each port in the range
for port in range (start_port, end_port+1):
    thread = threading.Thread(target = scan_port, args=(port,))
    thread.start()

print("\n>>>> Port scans complete.")
end_time = time.time()
print ( "Time elapsed: ", end_time-start_time)
exit()


