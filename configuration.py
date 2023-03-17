from subprocess import check_call
from sys import argv as args
if len(args) > 0:
    try:
        check_call(args[1:])
    except:
        pass
else:
    raise Exception('Missing argument: Shell command to run')