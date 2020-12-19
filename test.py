from logger import *

def test_all_log_levels():
    log(FATAL, "this is a fatal log")
    log(ERROR, "this is an error log")
    log(WARNING, "this is a warning log")
    log(INFO, "this is an info log")
    log(DEBUG, "this is a debug log")
    log(TRACE, "this is a trace log")

def test_all_log_levels_with_colors():
    log(FATAL, "this is a fatal log", style = STYLE.RED + STYLE.HL_GREEN)
    log(ERROR, "this is an error log", style = STYLE.RED + STYLE.HL_GREEN)
    log(WARNING, "this is a warning log", style = STYLE.RED + STYLE.HL_GREEN)
    log(INFO, "this is an info log", style = STYLE.RED + STYLE.HL_GREEN)
    log(DEBUG, "this is a debug log", style = STYLE.RED + STYLE.HL_GREEN)
    log(TRACE, "this is a trace log", style = STYLE.RED + STYLE.HL_GREEN)

if __name__ == "__main__":
    print("=======================")
    print("up to info, no prefix :")
    print("=======================")
    test_all_log_levels()
    test_all_log_levels_with_colors()

    Settings.log_level = TRACE
    print("========================")
    print("up to trace, no prefix :")
    print("========================")
    test_all_log_levels()
    test_all_log_levels_with_colors()

    Settings.log_level = INFO
    Settings.print_level_prefix = True
    print("=================================")
    print("up to info, with colored prefix :")
    print("=================================")
    test_all_log_levels()
    test_all_log_levels_with_colors()

    Settings.log_level = TRACE
    Settings.print_level_prefix = True
    print("==================================")
    print("up to trace, with colored prefix :")
    print("==================================")
    test_all_log_levels()
    test_all_log_levels_with_colors()

    Settings.print_level_prefix = True
    Settings.color_level_prefix = False
    print("====================================")
    print("up to TRACE, with uncolored prefix :")
    print("====================================")
    test_all_log_levels()
    test_all_log_levels_with_colors()

    Settings.log_level = TRACE
    Settings.print_level_prefix = True
    Settings.color_level_prefix = True
    Settings.indent = "\t"
    print("======================================================")
    print("up to trace, with colored prefix and indent for trace:")
    print("======================================================")
    test_all_log_levels()
    test_all_log_levels_with_colors()

    Settings.log_level = INFO
    Settings.print_level_prefix = True
    Settings.color_level_prefix = True
    Settings.indent = "\t"
    Settings.minimum_level_for_indent = FATAL
    print("===========================================")
    print("up to info, with colored prefix and indent:")
    print("===========================================")
    test_all_log_levels()
    test_all_log_levels_with_colors()
