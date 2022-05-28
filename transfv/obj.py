from . import constants

class Obj:

    def debug( self, message ):
        """Print message in a debug mode."""

        self.get_root().prints.debug( message )


    def get_root( self ):
        return constants.ROOT
