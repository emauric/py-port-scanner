import socket
import time
import sys
import threading

print_lock = threading.Lock()

def scan_ports(host_port):
    print(f"Scanning ports on {host_port}...")
    start_time = time.time()

    try:
        for port in range(1, 1025): # well known ports for testing purposes
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(.5)  # Set timeout on the socket instance
            result = s.connect_ex((host_port, port))

            if result == 0:
                print(f"[+] Port {port} is open")

            s.close()

        end_time = time.time()
        print(f"Scan completed in {end_time - start_time:.2f} seconds")

    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user (Ctrl+C)")
        sys.exit()

    except socket.error:
        print("\n[!] Couldn't connect to server.")
        sys.exit()

if __name__ == "__main__":
    target_page = input("Enter the host web address: ")
    try:
        target_host = socket.gethostbyname(target_page)
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved.")
        sys.exit()

    scan_ports(target_host)
