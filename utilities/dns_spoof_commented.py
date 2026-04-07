#!/usr/bin/env python

import netfilterqueue

def process_packet(packet):
    print(packet)
    # forward trapped packets to their destination
    packet.accept()

# Create an Instance "queue" of the netfilterqueue object
queue = netfilterqueue.NetfilterQueue()
# Invoke a method .bind() on the Object Instance we created
# Connect/bind the object to the queue "0".
# Assign a callback function "process_packet" to be executed on each packet trapped in queue "0".
queue.bind(0, process_packet)
# Run the queue
queue.run()