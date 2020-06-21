#!/usr/bin/env python3
from pathlib import Path


def main_menu(mainconn, stdin, stdout, stderr, debug):
    choices = {1:'Interact', 2:'Survey', 3:'Tunnels', 4:'Command Logs'}
    selection = choose_me(choices)
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