#!/usr/bin/env python
import subprocess
import sys

# This is an idea to run our iptables from a script, rather than manually in the terminal
# Just need more time to work around how to implement it, or even if it needs implementing

# Define the iptables command
# Create for the rule: iptables -I OUTPUT -j NFQUEUE --queue-num 0
output_cmd = [
    "iptables",
    "-I", "OUTPUT",
    "-j", "NFQUEUE",
    "--queue-num", "0",
    "--queue-bypass" # Optional: prevent packet loss if no listener running
]

# Create for the rule: iptables -I INPUT -j NFQUEUE --queue-num 0
input_cmd = [
    "iptables",
    "-I", "OUTPUT",
    "-j", "NFQUEUE",
    "--queue-num", "0",
    "--queue-bypass" # Optional: prevent packet loss if no listener running
]

def run_iptables_output():
    try:
        # Execute the commands
        output_result = subprocess.run(output_cmd, text=True)
        print("OUTPUT iptable added successfully: " + output_result.stdout)
    except subprocess.CalledProcessError as e:
        print("OUTPUT iptable failed")
        sys.exit(e.returncode)

def run_iptables_input():
    try:
        # Execute the commands
        input_result = subprocess.run(input_cmd, text=True)
        print("INPUT iptable added successfully: " + input_result.stdout)
    except subprocess.CalledProcessError as e:
        print("INPUT iptable failed")
        sys.exit(e.returncode)

if __name__ == "__run_iptable__":
    print("Print something...")