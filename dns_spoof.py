#!/usr/bin/env python

import netfilterqueue
from scapy.layers.inet import IP

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    print(scapy_packet.show())
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


