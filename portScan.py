'''
A simple script to scan for open ports.
'''
import sys
import time
import socket

def scan_host(start_port, end_port, host_ip):
	for port in range(start_port, end_port + 1):
		try:
			with socket.socket(socket.AF_INET, 
						socket.SOCK_STREAM) as sock:
            
				code = sock.connect_ex((host_ip, port))
				if code == 0:
					print("[*] Port {}: Open".format(port))
          
		except KeyboardInterrupt:
			print ("\n[!] Keyboard Interrupt, Exiting...")
			sys.exit(0)
		except Exception as e:
			print ("\n[!] Error: {}".format(e))
	return

def main():
	host = input("\n[*] Enter the Host to be Scanned: ")
	start_port = int(input("[*] Enter Start Port Number: "))
	end_port = int(input("[*] Enter End Port Number: "))

	print("\n[*] Scanning....")
	start_time = time.time()
	host_ip = socket.gethostbyname(host)

	scan_host(start_port, end_port, host_ip)        

	total_time = time.time() - start_time
	print("\n[*] Scanning Duration: {}".format(total_time))

if __name__ == "__main__":
	main()
  
