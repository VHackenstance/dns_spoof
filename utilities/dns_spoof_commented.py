#!/usr/bin/env python

import netfilterqueue
from scapy.layers.inet import IP
from scapy.layers.dns import DNSRR

def process_packet(packet):
    # Convert the packet to a scapy packet
    scapy_packet = IP(packet.get_payload())
    # Print the show of this packet
    # Use the haslayer method to check for DNS Response in packet
    if scapy_packet.haslayer(DNSRR):
        print(scapy_packet.show())
    # forward trapped packets to their destination
    packet.accept()

# Create an Instance "queue" of the netfilterqueue object
queue = netfilterqueue.NetfilterQueue()
# Invoke a method .bind() on the Object Instance we created
# Connect/bind the object to the queue "0".
# Assign a callback function "process_packet" to be executed on each packet trapped in queue "0".
queue.bind(0, process_packet)
# Run the queue
queue.run()