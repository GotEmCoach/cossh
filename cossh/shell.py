#!/usr/bin/env python3
import asyncio
from socket import socketpair

def reader(loop, rsock):
    data = rsock.recv()
    print(data)
    loop.remove_reader(rsock)
    loop.stop()


def remote_shell(stdin, stdout, stderr, debug):
    loop = asyncio.get_event_loop()
    rsock, wsock = socketpair()
    reader(loop, rsock)
    loop.add_reader(rsock, reader(loop, rsock))
    loop.add_writer(wsock, writer(loop, wsock))
    


