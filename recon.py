#!/usr/bin/env python

import subprocess

def print_bar():
	print("-" * 64)

def bash(command):
	return subprocess.check_output(['bash', '-c', command])

def nmap_scan(ip):
	print_bar()
	print("Scanning TCP ports on %s\n" % ip)
	res = bash('nmap -T4 -p1-65535 %s | grep open | grep -v "Discovered"' % ip).splitlines()
	ports = []
	for port in res:
		print(port)
		ports.append(port.split("/")[0])
	port_list = ",".join(ports)
	print("\nRunning intense scan on open ports...\n")
	bash('nmap -T4 -A -sV -p%s -oN output.txt %s' % (port_list, ip))
	print("Nmap intense scan results logged in 'output.txt'")
	exit()

ip_string = bash("ifconfig eth0 | grep 'inet '")
ip = ip_string.strip().split(' ')[1]
print_bar()
print("inet IPv4 address for networking interface eth0:\n%s\n" % ip)

octets = ".".join(ip.split(".")[:-1])
print("Running netdiscover on IP range %s.0-255" % octets)
ips = bash('netdiscover -P -r %s.0/24 | grep "1" | cut -d " " -f2' % octets).splitlines()

print_bar()
print("Choose an IP address to scan with Nmap:\n")
for i in range(0, len(ips)):
	ip = ips[i]
	print("%s - %s" % (i + 1, ip))
print("\n0 - Exit\n")
choice = input("Enter an option 1-%s, or 0 to exit the script:\n" % len(ips))
if (choice != 0):
	nmap_scan(ips[choice - 1])
else:
	exit()
