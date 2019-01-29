import sys; sys.dont_write_bytecode = True
import processor as dp
import commands as dc
import config as cfg
import colorama as colorama
from colorama import Fore, Back, Style

colorama.init()

def command_init(str):
    for i in range(len(cfg.symbols)):
        if str[:1] == list(cfg.symbols.items())[i][1]:
            if str in dc.COMMAND:
                dp.init(dc.COMMAND.get(str))
            elif str in cfg.COMMAND_SHORTCUT:
                dp.init(dc.COMMAND.get(cfg.COMMAND_SHORTCUT.get(str)))
            else:
                print(f"{Fore.RED}The command {Fore.WHITE}{str}{Fore.RED} doesn't exists.{Style.RESET_ALL}")

while cfg.actived:
    command_init(input("Command: ").lower())