#!/usr/bin/env python3
from pathlib import Path
import shell

async def main_menu(mainconn, stdin, stdout, stderr, debug):
    choices = {1:'Interact', 2:'Survey', 3:'Tunnels', 4:'Command Logs'}
    selection = choose_me(choices)
    if selection == 1:
        await interactive_menu(stdin, stdout, stderr, debug)
    print(selection)




def choose_me(choices):
    while True:
        print('Selection Choices\n')
        for key in choices:
            print(str(key) + ': ' + choices[key])
        selection = input('Choice: ')
        try:
            if int(selection) in choices.keys():
                return int(selection)
            else:
                print('\nIncorrect Selection, Choose a number from the menu!!!\n')
        except ValueError:
                print('\nA number was not selected, Please choose from the menu!!!\n')


async def interactive_menu(stdin, stdout, stderr, debug):
    choices = {1:'Remote', 2:'Local'}
    selection = choose_me(choices)
    if selection == 1:
        shell.remote_shell(stdin, stdout, stderr, debug)
    elif selection == 2:
        print('todo')
        #local_shell(debug)