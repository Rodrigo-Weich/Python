ID = 0
LINKS = {}
LASTLINKS = {}
LINKBYID = {}

symbols = {}
COMMAND_SHORTCUT = {}

symbols["exclamation"] = "!"
symbols["at"]          = "@"
symbols["fence"]       = "#"
symbols["dollar sign"] = "$"
symbols["copyright"]   = "©"

actived = True
time_search     = 900           #15 Minutes
max_amount      = 99999

available_sites = [
    "Americanas",
    "Submarino",
    "Shoptime",
    "Magazine Luiza",
    "Walmart",
    "Amazon"
]

COMMAND_SHORTCUT["@set"]            = "@setlink"
COMMAND_SHORTCUT["@unset"]          = "@unsetlink"
COMMAND_SHORTCUT["@unsetall"]       = "@clearlinks"
COMMAND_SHORTCUT["@cmds"]           = "@commands"
COMMAND_SHORTCUT["@cl"]             = "@clearlinks"
COMMAND_SHORTCUT["@cc"]             = "@clearcon"
COMMAND_SHORTCUT["@st"]             = "@searchtime"