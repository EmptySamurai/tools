import socket
import sys
from contextlib import closing

TIMEOUT = 5 #seconds

host = sys.argv[1]

def check_port(host, port):
	with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
		sock.settimeout(TIMEOUT)
		result = sock.connect_ex((host,port))
		if result==0:
			return "Open"
		elif result == 11 or result == 110:
			return "Timeout"
		else:
			return "Closed"

text_colors = {
"RED"   : "\033[1;31m",
"BLUE"  : "\033[1;34m",
"CYAN"  : "\033[1;36m",
"GREEN" : "\033[0;32m",
"RESET" : "\033[0;0m",
"BOLD"    : "\033[;1m",
"REVERSE" : "\033[;7m",
}

def colorize_text(text, color):
	return text_colors[color]+text+text_colors["RESET"]

common_ports = {
21: "FTP",
22: "SSH",
23: "TELNET",
25: "SMTP",
53: "DNS",
80: "HTTP",
110: "POP3",
115: "SFTP",
135: "RPC",
139: "NetBIOS",
143: "IMAP",
194: "IRC",
443: "SSL",
445: "SMB",
1433: "MSSQL",
3306: "MySQL",
3389: "Remote Desktop",
5432: "Postgres",
5632: "PCAnywhere",
5900: "VNC",
8080: "Debug"
}

if len(sys.argv)>2:
	ports = {int(port) : "" for port in sys.argv[2:]}
else:
	ports = common_ports

for port, port_name in ports.items():
	status =  check_port(host, port)
	text = "{0} {1}: {2}".format(port, port_name, status)

	if status == "Open":
		text = colorize_text(text, "GREEN")
	elif status == "Closed":
		text = colorize_text(text, "RED")
	elif status == "Timeout":
		text = colorize_text(text, "BLUE")
	print(text)
