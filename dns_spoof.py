#!/usr/bin/env python2
import netfilterqueue
from scapy.layers.inet import IP
from scapy.layers.dns import DNSRR, DNSQR, DNS, UDP

target_ip_vm = " 192.168.63.174"
target_interface_vm = "Ethernet0"

def process_packet():
    print("Process Packet.")

process_packet()


