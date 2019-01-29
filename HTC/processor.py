import commands
import config as cfg
import colorama as colorama
from colorama import Fore, Back, Style

colorama.init()

def load_def(str):
    try:
        str = "commands." + str
        exec(str)
    except:
        print(f"Err {str}")

def init(args):
    t_args          = args.split("|")
    v_level         = int(t_args[0])
    v_shortcut      = t_args[1]
    v_msg           = t_args[2]
    v_event         = t_args[3]

    if v_level >= 1:
        print(Fore.RED + "You can't use this command." + Style.RESET_ALL)
    else:     
        if v_msg != "None":
            if v_shortcut != "None":
                print(Fore.LIGHTYELLOW_EX + v_msg + Style.RESET_ALL)
                print(Fore.LIGHTYELLOW_EX + f"Command shortcut: {v_shortcut}." + Style.RESET_ALL)
                load_def(v_event)
            else:
                print(Fore.LIGHTYELLOW_EX + v_msg + Style.RESET_ALL)
                load_def(v_event)
        else:
            load_def(v_event)