#!/usr/bin/env python

import sys
import subprocess
import time

if (len(sys.argv) < 2):
	print("Call scanner with a target IP address")
	print("Usage: scanner <ip> ?<output_file>")
	exit()

scan_time = time.strftime('%Y-%m-%d_%H.%M.%S')
init_time = time.strftime('%l:%M %p %Z on %b %d, %Y')
print("-" * 64 + "\nScanning ports on {} at{}\n".format(sys.argv[1], init_time) + "-" * 64)

command = ["nmap", "-F", "-oG", sys.argv[1]]
if (len(sys.argv) < 3):
	write_path = str(scan_time) + ".nmap"
	command.insert(3, write_path)
else:
	command.insert(3, sys.argv[2])

res = subprocess.check_output(command)

for line in res.splitlines()[2:]:
	print(line)

if (len(sys.argv) == 3):
	print("Nmap scan output logged in {}".format(sys.argv[2]))
else:
	print("Nmap scan output logged in {}.nmap".format(str(scan_time)))

sys.exit()
exit()
