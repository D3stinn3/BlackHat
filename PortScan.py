import nmap
import ipaddress
import os
import re

while True:
    
    global my_ipaddr
    
    my_ipaddr = input("\nPlease input ip addr: ")
    
    try:
        ip_object = ipaddress.ip_address(my_ipaddr)
        print("Hii ni ip address ya ukweli!")
        break
        
    except:
        print("Hii si ip address ya ukweli!")
        
while True:
    port_min = 0
    port_max = 65535
    port_range = input("\nTafadhali weka port range(Example 80-90): ")
    
    try:
        port_range_pattern = re.compile("([0-9]+) - ([0-9]+)")
        port_range_refined = port_range.replace(" ", "")
        port_range_validity = port_range_pattern.search(port_range_refined)
        
        if port_range_validity:
            print("Valid port range!")
            
            global port_listing
            
            port_upper_limit = int(port_range_validity.group(1))
            port_lower_limit = int(port_range_validity.group(2))
            port_listing = (port_lower_limit, port_upper_limit + 1)
        break
        
    except:
        print("Invalid port range scan values")
        

def portscanner():
    
    port_scanner = nmap.PortScanner()
    
    for port in range(port_listing):
        
           try:
               result = port_scanner.scan(my_ipaddr, str(port))
               
               print(f"{result} becomes the desired dict")
               
               port_status = (result["scan"][my_ipaddr]["tcp"][port]["state"])
               print(f"{port} is {port_status}")
               
           except:
               print(f"Siezi scan {port}")
               
               
               
if __name__ == "main":
    portscanner()