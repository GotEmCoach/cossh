#!/usr/bin/env python3
import asyncssh


def initialize(mainconn, mainchan, mainsession, debug):
    if debug == True:
        checks = ['username', 'client_version', 'server_version', 
                    'send_cipher', 'send_mac', 'send_compression', 'recv_cipher', 'recv_mac',
                    'recv_compression']
        for item in checks:
            print(item + ': ' + mainconn.get_extra_info(item))
        #for key in envdict:
        #   print(key + ': ', envdict[key])
    return
    