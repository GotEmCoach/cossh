#!/usr/bin/env python3
import asyncio
from socket import socketpair
import asyncssh

def writer():

def reader():
    while stopped = False:
        data = rsock.recv(100)
        print(data)


def remote_shell(initshell, rsock, wsock, loop, debug):
    print('env variables =')
    print(initshell[0])
    print(initshell[0].get_environment())
    print(initshell[1])
    reader = initshell[1]
    writer = initshell[0]
    await readandwrite(loop, rsock, wsock)


async def readandwrite(loop, rsock, wsock):
    stopped = False
    loop.add_reader(rsock, reader)
    try:
        loop.run_forever()
    except Exception as e:
        print(repr(e))
    


    

