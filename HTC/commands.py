import request as dr
import os, time
import config as dc
import request as rq
import colorama as colorama
from colorama import Fore, Back, Style

colorama.init()

COMMAND = {}

def _exit():
    print("Closing..")
    rq.time_sleep(2)
    dc.actived = False

def _setlink():
    link = input("Link: ").lower()
    if link[:7] == "http://" and link[7:] != "" or link[:8] == "https://" and link[8:] != "" or link[:4] == "www." and link[4:] != "":
        dc.LINKS[dc.ID] = link
        dc.ID += 1
        print(f"{Fore.GREEN}Link {Fore.WHITE}{link[:100]}{Fore.GREEN} added successfully.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}The link isn't valid. Try again.{Style.RESET_ALL}")
        _setlink()

def _unsetlink():
    if len(dc.LINKS) != 0:
        id = int(input("Link ID: "))
        if id in dc.LINKS:
                print(f"The link {dc.LINKS[id]} has been deleted!")
                del dc.LINKS[id]
        else:
                print(f"{Fore.RED}Please enter a valid key.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}The list is empty.{Style.RESET_ALL}")

def _links():
    if len(dc.LINKS) != 0:
        for i,s in dc.LINKS.items():
             print(f"{i} | {s}")
    else:
        print(f"{Fore.RED}The list is empty.{Style.RESET_ALL}")

def _commandlist():
    if len(COMMAND) != 0:
        print(f"COMMAND \t SHORTCUT")
        for key in COMMAND.keys():
            for _key, _item in dc.COMMAND_SHORTCUT.items():
                if _item == key:
                    print(f"{key} \t {_key}")
                    break
            if _item != key:
                print(key)
    else:
        print(f"{Fore.RED}There are no commands yet.{Style.RESET_ALL}")

def _clearlist():
    if len(dc.LINKS) != 0:
        dc.LINKS.clear()
    else:
        print(f"{Fore.RED}The list is empty.{Style.RESET_ALL}")

def _clearcon():
    os.system('cls' if os.name=='nt' else 'clear')

def _startlist():
    sender = []
    if len(dc.LINKS) != 0:
        amount = int(input("Number of searches: "))
        if amount > dc.max_amount:
            print(f"{Fore.LIGHTGREEN_EX}Invalid amount. Your/Max: {Fore.WHITE}{amount}/{dc.max_amount}{Fore.LIGHTGREEN_EX}.{Style.RESET_ALL}")
        else:
            for i, j in dc.LINKS.items():
                sender.append(j)
            rq.get_requests(sender, amount)
    else:
        print("The list is empty.")

def _searchtime():
     try:
        time = float(input("Time to search [minutes]: "))
        dc.time_search = time*60
        print(f"{Fore.GREEN}New update time: {Fore.WHITE}{time}{Fore.GREEN} minutes.{Style.RESET_ALL}")
     except:
        dc.time_search = 900
        print(f"{Fore.GREEN}Standard update time: {Fore.WHITE}{dc.time_search}{Fore.GREEN}. {Fore.WHITE}{dc.time_search/60}{Fore.GREEN} minutes.{Style.RESET_ALL}")

def _weblist():
    for item in dc.available_sites:
        print(item)

COMMAND["@exit"]                   = "0|None|None|_exit()"
COMMAND["@setlink"]                = "0|@set|Use http://, https:// or www. links.|_setlink()"
COMMAND["@unsetlink"]              = "0|@unset|Select Link by ID|_unsetlink()"
COMMAND["@links"]                  = "0|None|None|_links()"
COMMAND["@commands"]               = "0|@cmds|None|_commandlist()"
COMMAND["@clearlinks"]             = "0|@cl|None|_clearlist()"
COMMAND["@clearcon"]               = "0|@cc|None|_clearcon()"
COMMAND["@start"]                  = "0|None|Define the amount of searches to perform.|_startlist()"
COMMAND["@searchtime"]             = "0|@st|Set the interval time for each search|_searchtime()"
COMMAND["@weblist"]                = "0|@wl|Available sites|_weblist()"