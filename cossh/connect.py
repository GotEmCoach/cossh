#!/usr/bin/env python3

import asyncssh
import sys
import asyncio
import argparse
import shlex
import subprocess
import logic



class mainsession(asyncssh.SSHTCPChannel):
	"""docstring for mainsession"""
    def data_received(self, data, datatype):
        # We use sys.stdout.buffer here because we're writing bytes
        sys.stdout.buffer.write(data)

    def connection_lost(self, exc):
        if exc:
            print('Direct connection error:', str(exc), file=sys.stderr)
		

async def run_client(port, host, user, passw):
        session = await asyncssh.connect(host, port=port, password=passw, username=user, 
    							known_hosts=None)
        
        mainchan = await conn.create_tcp_channel(encoding='utf-8')
        while True:
            logic(mainchan)



def main(args)
	try:
    	asyncio.get_event_loop().run_until_complete(run_client(args.port, args.host, args.user, args.passw))
	except (OSError, asyncssh.Error) as exc:
    	sys.exit('SSH connection failed: ' + str(exc))

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument('-p', '--port', dest=port, help='remote port to connect', default=22, type=int)
    args.add_argument('-n', '--hostname', dest=host, help='hostname or IP Address', type=str)
    args.add_argument('--pass', dest=passw, help='password to authenticate', type=str)
    args.add_argument('--user', dest=user, help='username to authenticate', type=str)
    main(args)
	#### TO DO: ARGPARSER #####
