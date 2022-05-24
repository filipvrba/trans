from . import constants

class Events:

    def __init__( self, transfv ) -> None:
        self.transfv = transfv


    def help( self, object, arg ):
        self.transfv.helper()


    def message( self, object, arg ):
        object.set_value( arg )


    def first( self, object, arg ):

        if arg == constants.GET:
            print(self.transfv.configuration.get_first_lang_config())
        else:
            object.set_value( arg )


    def second( self, object, arg ):

        if arg == constants.GET:
            print(self.transfv.configuration.get_second_lang_config())
        else:
            object.set_value( arg )


    def open( self, object, arg ):
        object.set_value( True )


    def value( self, object, arg ):
        object.set_value( True )


    def images( self, object, arg ):
        object.set_value( True )