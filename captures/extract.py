#!/usr/bin/env python3

from scapy.all import rdpcap, TCP, NoPayload
import sys

pcap = rdpcap(sys.argv[1])
last_port_seen = 0
count = 0

for pkt in pcap:
    if TCP in pkt and type(pkt[TCP].payload) != NoPayload:
        if pkt[TCP].dport != last_port_seen:
            last_port_seen = pkt[TCP].dport
            count += 1
        with open('payload-%02d.%s.data' % (count, 'c' if count % 2 else 's'), 'ab') as f:
            f.write(bytes(pkt[TCP].payload))
