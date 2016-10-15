import socket
import sys
import time

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

HOST = '10.0.0.1';
PORT = 5555;

bitsPerSecond = 1400000
bytesPerSecond = bitsPerSecond / 8
leadingSegID = 0

try:
    while True:
        msg = (str(leadingSegID) + " " + "a"*65000)
        s.sendto(msg, (HOST, PORT))
        print 'Sent packet with leadingSegID ' + str(leadingSegID)
        leadingSegID += 1
        time.sleep(float(len(msg))/bytesPerSecond)


finally:
    print 'Closing socket'
    s.close();
