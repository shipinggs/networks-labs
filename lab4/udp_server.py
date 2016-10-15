import socket
import sys

HOST = '10.0.0.1'   # Symbolic name meaning all available interfaces
PORT = 5555 # Arbitrary non-privileged port

# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket.'
    sys.exit()
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed.'
    sys.exit()

print 'Socket bind complete. Waiting to receive message...'

MAX_WAITING_QUEUE_SIZE = 10;
expectedLeadingSegID = 0
missingPackets = []

while True:
    d = s.recvfrom(4096)
    data = d[0]
    leadingSegID = int(data.split()[0])
    print 'Received packet ' + str(leadingSegID)

    if leadingSegID != expectedLeadingSegID:
        if leadingSegID in missingPackets:
            missingPackets.remove(leadingSegID);
        else:
            while expectedLeadingSegID < leadingSegID:
                missingPackets.append(expectedLeadingSegID)
                expectedLeadingSegID += 1

    if len(missingPackets) > 0:
        while missingPackets[0] < leadingSegID - MAX_WAITING_QUEUE_SIZE:
            print 'Warning: Packet ' + str(missingPackets[0]) + ' was dropped'
            missingPackets.remove(missingPackets[0])

    expectedLeadingSegID += 1
    print(missingPackets)
