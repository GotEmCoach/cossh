#!/usr/bin/env python3
import asyncio
from socket import socketpair
import asyncssh


async def remote_shell(initshell, debug):
    print(initshell.channel)
    await initshell.redirect(stdin=mywriter, stdout=myreader, stderr=myreader)
    while True:
        userin = input
        mywriter.write(userin)






class mywriter(asyncssh.SSHSubprocessWritePipe):
    def __init__(self, SSHProcess, SSHClientStreamSession):
        super().__init__(SSHProcess, SSHClientStreamSession)

class myreader(asyncssh.SSHSubprocessReadPipe):
    def __init__(self, SSHProcess, SSHClientStreamSession):
        super().__init__(SSHProcess, SSHClientStreamSession)

    

