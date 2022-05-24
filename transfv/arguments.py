import sys, getopt
from . import constants
from .events import Events


class Arguments:

    def __init__( self, transfv ) -> None:
        self.transfv = transfv
        self.argument = sys.argv[1:]
        self.events = Events( transfv )

        self.arguments = [
            constants.ARGUMENTS[0].set_callback( self.events.help ),
            constants.ARGUMENTS[1].set_callback( self.events.message ),
            constants.ARGUMENTS[2].set_callback( self.events.first ),
            constants.ARGUMENTS[3].set_callback( self.events.second ),
            constants.ARGUMENTS[4].set_callback( self.events.open ),
            constants.ARGUMENTS[5].set_callback( self.events.value ),
            constants.ARGUMENTS[6].set_callback( self.events.images ),
        ]


    def get_short_arguments( self ):

        opts = ""
        for argument in self.arguments:

            opts += argument.get_short_opt()
        
        return opts

    def get_long_arguments( self ):

        opts = []
        for argument in self.arguments:
            
            opt = argument.get_long_opt()

            if opt:
                opts.append( opt )

        return opts


    def set_vars_from_args( self ):

        try:
            opts, args = getopt.getopt( self.argument,
            self.get_short_arguments(),
            self.get_long_arguments() )
    
        except getopt.GetoptError:
            self.transfv.exit_app( 2 )

        for opt, arg in opts:
            for argument in self.arguments:

                if opt in argument.get_full():
                    argument.emit( argument, arg )
