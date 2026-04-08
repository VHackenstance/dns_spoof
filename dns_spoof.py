#!/usr/bin/env python

import netfilterqueue
from scapy.layers.inet import IP
from scapy.layers.dns import DNSRR

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    # Use the haslayer method to check for DNS Response in packet
    if scapy_packet.haslayer(DNSRR):
        print(scapy_packet.show())
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


