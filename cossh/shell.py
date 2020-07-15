#!/usr/bin/env python3
import asyncio
from socket import socketpair
import asyncssh

async def writer(session):
    print('this')

async def shellloop(initshell, debug):
    await initshell[0].wait_closed()
    await writer(initshell[1])



async def remote_shell(initshell, debug):
    try:    
        await shellloop(initshell, debug)
    except (OSError, asyncssh.Error) as exc:
        print(exc)
        return   


    

