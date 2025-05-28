import socket
import time
import sys
import concurrent.futures


def scan_port(host_port, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(.5)  # Set timeout on the socket instance
        result = s.connect_ex((host_port, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user (Ctrl+C)")
        sys.exit()
    except socket.error:
        print("\n[!] Couldn't connect to server.")
        sys.exit()


def scan_ports(host_port):
    print(f"scanning ports on {target_page}...")
    start_time = time.time()
    ports_to_scan = range(1, 1025)
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports_to_scan:
            executor.submit(scan_port, host_port, port)
    end_time = time.time()
    print(f"\n scan completed in  {end_time - start_time: .2f} seconds.")


if __name__ == "__main__":
    target_page = input("Enter the host web address: ")
    try:
        target_host = socket.gethostbyname(target_page)
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved.")
    scan_ports(target_host)
    sys.exit()
