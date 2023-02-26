from socket import socket, AF_INET, SOCK_STREAM, timeout
import time
from typing import List, Dict
from datetime import datetime


class PortScanner:

    def __init__(self, timeout_secs:float = 5.0):
        self.listener = self.initialize_socket(timeout_secs)

    def initialize_socket(self, timeout_secs: float):
        # A network socket is an endpoint for sending and receiving data
        # Identified by both the IP address and the port
        # https://www.geeksforgeeks.org/socket-in-computer-network/

        # AF_INET - configuring the socket to use IPv4
        # SOCK_STREAM - Use TCP to send packets
        listener = socket(AF_INET, SOCK_STREAM)

        # We set the timeout
        listener.settimeout(timeout_secs)

        return listener

    def check_port(self, target_ip: str, target_port: int) -> bool:
        
        try:
            # We try to connect to the reciever using the IP and port in the parameters.
            # Connect_ex will return a 0 if we successfully made the connection, a integer otherwise
            error_code = self.listener.connect_ex((target_ip, target_port))
            return error_code == 0
        except timeout:
            # If we timed out, return false
            return False
    
    def check_ports_in_range(self, target_ip: str, start_port: int, end_port):
        # Create a list of all ports to check starting from start_port and ending at end_port inclusive
        for port in range(start_port, end_port+1):
            if self.check_port(target_ip, port):
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")

    def launch_scan(self):
        # The input function gets input from the user and returns it as a string
        target_ip = input("Enter a target to scan: ")
        print("Please enter the range of ports you would like to scan on the target")
        
        # We need to convert the start port and end port to integers
        start_port = int(input("Enter a start port: "))
        end_port = int(input("Enter an end port: "))

        # The datetime.now() gives us the current date and time for the timestamp
        print(f"Scanning started at {datetime.now()}")

        self.check_ports_in_range(target_ip=target_ip, start_port=start_port, end_port=end_port)
        
        # Stop our socket from listening and free up the port
        self.listener.close()



def main():
    server = PortScanner()
    server.launch_scan()


if __name__ == "__main__":
    main()
