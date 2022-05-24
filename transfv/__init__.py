#!/usr/bin/python

import sys
from . import constants
from .prints import Prints
from .translator import Translator
from .configuration import Configuration
from .thirdside import ThirdSide
from .arguments import Arguments

class App:

    def __init__( self ):

        self.prints = Prints()
        self.translator = Translator( self )
        self.configuration = Configuration()
        self.thirdside = ThirdSide( self )
        self.arguments = Arguments( self )

        self.prints.debug("init app")


    def exit_app( self, value = 0 ):
        sys.exit( value )


    def helper( self ):
        self.prints.helper()
        self.exit_app()


    def clear( self ):

        self.prints.clear()
        self.translator.clear()


    def info( self ):
        self.prints.print_informations()
    

    def open( self ):
        self.thirdside.open_google_trans()
    

    def value( self ):

        if self.thirdside.open_google():
                self.prints.print_nots_value()
    

    def images( self ):
        self.thirdside.open_google_images()

    
    def help( self ):
        self.prints.print_helps()


    def checkFunction( self, text ):

        if ( text == constants.EXIT ):
            self.exit_app()
        elif ( text == constants.CLEAR ):
            self.clear()
            self.info()
            return True
        elif ( text == constants.INFO ):
            self.info()
            return True
        elif ( text == constants.OPEN ):
            self.open()
            return True
        elif ( text == constants.OPEN_ALL ):
            self.value()
            self.open()
            self.images()
            return True
        elif ( text == constants.VALUE ):
            self.value()
            return True
        elif ( text == constants.IMAGES ):
            self.images()
            return True
        elif ( text == constants.HELP ):
            self.help()
            return True
        else:
            self.clear()
            self.info()
        
        return False


    def main( self ):
        self.arguments.set_vars_from_args()
        self.configuration.check_languages()

        self.scenario( self.arguments.argument )


    def scenario( self, argument ):

        if ( not argument ):
            self.prints.print_informations()
            self.translator.translation_loop()
        else:
            message = constants.ARGUMENTS[1]
            open = constants.ARGUMENTS[4]
            value = constants.ARGUMENTS[5]
            images = constants.ARGUMENTS[6]

            if open.value or value.value or images.value:
                if message.value:
                    self.prints.debug( "set history" )
                    self.translator.history.set_text( message.value )
                    self.translator.detectDect( message.value )

            if open.value:
                self.prints.debug("open translator")
                self.checkFunction( constants.OPEN )
            else:
                self.prints.debug("translate")
                self.translator.translate( message.value )
            
            if value.value and not open.value:
                self.prints.debug("open value")
                self.checkFunction( constants.VALUE )
            elif value.value and open.value:
                self.prints.debug(f"{ constants.LAST_LINE }translate")
                self.translator.translate( message.value )
                self.prints.debug("open value")
                self.checkFunction( constants.VALUE )
            
            if images.value:
                self.prints.debug("open images")
                self.checkFunction( constants.IMAGES )
