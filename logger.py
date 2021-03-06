FATAL = 0
ERROR = 1
WARNING = 2
INFO = 3
DEBUG = 4
TRACE = 5

level_prefixes = [
    "[FATAL]  :",
    "[ERROR]  :",
    "[WARNING]:",
    "[INFO]   :",
    "[DEBUG]  :",
    "[TRACE]  :"
]

colored_level_prefixes = [
    "\033[41;37;1m[FATAL]\033[0m  \033[31m:\033[0m",
    "\033[31;1m[ERROR]  :\033[0m",
    "\033[33m[WARNING]:\033[0m",
    "\033[32m[INFO]   :\033[0m",
    "\033[36m[DEBUG]  :\033[0m",
    "\033[37m[TRACE]  :\033[0m",
]


class Settings:
    log_level = INFO
    print_level_prefix = False
    color_level_prefix = True
    minimum_level_for_indent = TRACE
    indent = ""

class STYLE:
    BLACK      = "\033[30m"
    RED        = "\033[31m"
    GREEN      = "\033[32m"
    YELLOW     = "\033[33m"
    BLUE       = "\033[34m"
    MAGENTA    = "\033[35m"
    CYAN       = "\033[36m"
    WHITE      = "\033[37m"

    HL_BLACK   = "\033[40m"
    HL_RED     = "\033[41m"
    HL_GREEN   = "\033[42m"
    HL_YELLOW  = "\033[43m"
    HL_BLUE    = "\033[44m"
    HL_MAGENTA = "\033[45m"
    HL_CYAN    = "\033[46m"
    HL_WHITE   = "\033[47m"

    BOLD       = "\033[1m"
    UNDERLINED = "\033[4m"

    RESET      = "\033[0m"


def log(level, *args, **kwargs):
    if level <= Settings.log_level:
        if Settings.print_level_prefix:
            if Settings.color_level_prefix:
                print(colored_level_prefixes[level], end="")
            else:
                print(level_prefixes[level], end="")
        style = False
        if "style" in kwargs:
            style = True
            print(kwargs["style"], end="")
            kwargs.pop("style")
            if "end" in kwargs:
                kwargs["end"] = STYLE.RESET + kwargs["end"]
            else:
                kwargs["end"] = STYLE.RESET + "\n"

        if level >= Settings.minimum_level_for_indent:
            print(Settings.indent, end="")
        print(*args, **kwargs)
