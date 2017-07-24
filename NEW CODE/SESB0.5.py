__version__ = "0.5"

from engine import *
import sys

start = Engine()
start.check()

if len(sys.argv) > 1:
    print "As of 0.5+, the only way to config your script is to use config.cfg"
    print "Because yeah, i don't see why anyone would want to retype everything again-"
    print "-once they want to reuse the script. It's silly."
    print "You can still use 0.4, check \"OLD CODE\""
    exit(0)

else:
    try:
        print "Started the script."
        start.thespam()
    except KeyboardInterrupt:
        print "Stopped the script.."
