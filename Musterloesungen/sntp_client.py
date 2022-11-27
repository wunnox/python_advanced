#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:20:23 2022

@author: rene.degen@inodes.ch
"""

import socket
import struct, time

NTP_SERVER = 'ntp.3eck.net'
NTP_PORT = 123
# reference time (in seconds since 1900-01-01 00:00:00)
TIME1970 = 2208988800 # 1970-01-01 00:00:00

 
def sntp_client(host = NTP_SERVER, port = NTP_PORT):
        buf = 1024
        address = (host,port)
        data = '\x1b' + 47 * '\0'
  
        # connect to server
        with socket.socket( socket.AF_INET, socket.SOCK_DGRAM) as client:
            client.sendto(data.encode('utf-8'), address)
            data, address = client.recvfrom( buf )
 
        t = struct.unpack( "!12I", data )[10]
        t -= TIME1970
        return time.strftime('%Y-%m-%d %H:%M:%S')    
 
if __name__ == "__main__":
        print(sntp_client())
