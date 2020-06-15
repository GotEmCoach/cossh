#!/usr/bin/env python3

import asyncssh
import sys
import asyncio
import argparse
import shlex
import subprocess




class mainsession(asyncssh.SSHTCPChannel):
	"""docstring for mainsession"""
    def data_received(self, data, datatype):
        # We use sys.stdout.buffer here because we're writing bytes
        sys.stdout.buffer.write(data)

    def connection_lost(self, exc):
        if exc:
            print('Direct connection error:', str(exc), file=sys.stderr)
		

async def run_client(port, host, user, passw):
    async with asyncssh.connect(host, port=port, password=passw, username=user, 
    							known_hosts=None) as conn:
    	extrainfo = await conn.get_extra_info(conn.set_extra_info())
        mainchan = await conn.create_tcp_channel(encoding='utf-8')
        while True:
        	cmd = 
        	mainchan.write()



def main()
	try:
    	asyncio.get_event_loop().run_until_complete(run_client())
	except (OSError, asyncssh.Error) as exc:
    	sys.exit('SSH connection failed: ' + str(exc))

if __name__ == "__main__":
	#### TO DO: ARGPARSER #####
