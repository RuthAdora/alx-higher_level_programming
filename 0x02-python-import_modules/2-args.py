#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    if (arg <= 1):
        print("{} arguements.".format(arg - 1))
    elif (arg == 2):
        print("{} arguement:".format(arg - 1))
    else:
        print("{} arguements:".format(arg - 1))
    for arg_c in range(1, arg):
        print("{}: {}".format(arg_c, sys.argv[arg_c]))
