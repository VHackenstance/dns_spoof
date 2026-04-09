#!/usr/bin/env python

import netfilterqueue
from scapy.layers.inet import IP
from scapy.layers.dns import DNSRR, DNSQR

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        qname = scapy_packet[DNSQR].qname
        qname_str = qname.decode('utf-8')
        if "www.bing.com" in qname_str:
            print("[+] Spoofing Target is in: " + qname_str )
            # **** Here we can put our code to redirect the User somewhere else **** #

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


