#!/usr/bin/env python3

def initialize(mainconn, stdin, stdout, stderr, debug):
    try:
        if debug == True:
            print(mainconn)
            checks = ['username', 'client_version', 'server_version', 
                        'send_cipher', 'send_mac', 'send_compression', 'recv_cipher', 'recv_mac',
                        'recv_compression']
            for item in checks:
                print(item + ': ' + mainconn.get_extra_info(item))
            thethree = [stdin, stdout, stderr]
            for i in thethree:
                print(i.channel)
                for item in checks:
                    print(item + ': ' + i.get_extra_info(item)) 
        print('Connection has been successfully made!\n')
        return
    except:
        return
    