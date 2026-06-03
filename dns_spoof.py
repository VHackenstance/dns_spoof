#!/usr/bin/env python2
# Rebuild
import netfilterqueue
from scapy.layers.inet import IP
from scapy.layers.dns import DNSRR

target_ip_vm = "192.168.63.174"
target_interface_vm = "Ethernet0"
new_target_ip = "192.168.63.139"
target_DN = "www.pentest-standard.org"
# 44.238.29.244
# rrname = 'pentest-standard.org'
# rdata = 96.126.116.56

def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        print(scapy_packet.show())
        # packet.drop()
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()