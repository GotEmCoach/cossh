#!/usr/bin/env python3

import asyncssh
import sys
import asyncio
import argparse
import shlex
import subprocess
from initialization import *

async def run_client(port, host, user, passw, debug):
    session = await asyncssh.connect(host, port=port, password=passw, username=user,known_hosts=None)
    mainchan, mainsession = await session.create_session()
    while True:
        initialize(mainchan, mainsession)


def main(args):
    try:
        asyncio.get_event_loop().run_until_complete(run_client(args.port, args.host, args.user, args.passw, args.debug))
    except (OSError, asyncssh.Error) as exc:
        sys.exit('SSH connection failed: ' + str(exc))

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument('-p', '--port', dest=port, help='remote port to connect', default=22, type=int)
    args.add_argument('-n', '--hostname', dest=host, help='hostname or IP Address', type=str)
    args.add_argument('--pass', dest=passw, help='password to authenticate', type=str)
    args.add_argument('--user', dest=user, help='username to authenticate', type=str)
    args.add_argument('--debug', dest=debug, help='Turns debug mode on', type=bool, const=True)
    args.parse_args()
    main(args)
	#### TO DO: ARGPARSER #####
