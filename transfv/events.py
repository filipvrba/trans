from . import constants

class Events:

    def __init__( self, transfv ) -> None:
        self.transfv = transfv


    def help( self, object, arg ):
        self.transfv.helper()


    def message( self, object, arg ):
        object.set_value( arg )

        self.transfv.prints.debug( "set history" )
        self.transfv.translator.history.set_text( arg )
        self.transfv.translator.detectDect( arg )

        self.transfv.prints.debug("translate")
        self.transfv.translator.translate( arg )
        self.transfv.save_translations()


    def first( self, object, arg ):

        if arg == constants.GET:
            print(self.transfv.configuration.get_first_lang_config())
        else:
            object.set_value( arg )
            self.transfv.configuration.check_languages()


    def second( self, object, arg ):

        if arg == constants.GET:
            print(self.transfv.configuration.get_second_lang_config())
        else:
            object.set_value( arg )
            self.transfv.configuration.check_languages()


    def open( self, object, arg ):
        object.set_value( True )

        self.transfv.prints.debug("open translator")
        self.transfv.checkFunction( constants.OPEN )


    def value( self, object, arg ):
        object.set_value( True )

        self.transfv.prints.debug("open value")
        self.transfv.checkFunction( constants.VALUE )


    def images( self, object, arg ):
        object.set_value( True )

        self.transfv.prints.debug("open images")
        self.transfv.checkFunction( constants.IMAGES )
    

    def info( self, object, arg ):
        self.transfv.prints.print_informations()
