#!/usr/bin/env python2
import netfilterqueue
from scapy.layers.inet import IP
from scapy.layers.dns import DNSRR, DNSQR, DNS, UDP

target_ip_vm = " 192.168.63.174"
target_interface_vm = "Ethernet0"
new_target_ip = "192.168.63.139"
target_DN = "testasp.vulnweb.com"


def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        qname = scapy_packet[DNSQR].qname
        if target_DN in qname:
            print("[+] Spoofing Target: " + target_DN)

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
