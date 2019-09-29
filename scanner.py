#!/usr/bin/env python

import sys
import subprocess
import datetime

if (len(sys.argv) < 2):
	print("Call scanner with a target IP address")
	print("Usage: scanner <ip> ?<output.file>")
	exit()

print("Scanning ports of IP address {}".format(sys.argv[1]))
command = ["nmap", "-oG", sys.argv[1]]
if (len(sys.argv) < 3):
	command.insert(2, "res.txt")
else:
	command.insert(2, sys.argv[2])

res = subprocess.check_output(command)

# uncomment to display nmap output to terminal
# ---------------------------------------------
#for line in res.splitlines():
#	print(line)

if (len(sys.argv) == 3):
	print("Results of nmap scan stored in {}".format(sys.argv[2]))
else:
	print("Results of nmap scan stored in res.txt")

sys.exit()
exit()
