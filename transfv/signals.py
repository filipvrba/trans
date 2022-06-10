import signal
from . import constants

class Signals:
    def __init__(self):

        def connect():
            signal.signal( signal.SIGINT, self.intHandler )
        connect()


    def intHandler( self, signum, frame ):
        print()
        constants.ROOT.checkFunction( constants.EXIT )
