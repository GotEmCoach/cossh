#!/usr/bin/env python3
import asyncssh


def initialize(mainchan, mainsession, debug):
    if debug == True:
        print(mainchan.get_extra_info(username, client_version, server_version, 
                    send_cipher, send_mac, send_compression, recv_cipher, recv_mac,
                    recv_compression))
        envdict = mainchan.get_environment()
        for key in envdict:
            print(key + ': ', envdict[key])
        print(mainsession.get_write_buffer_size())
    
    return
    