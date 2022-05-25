from . import constants
import googletrans

class History:

    def __init__( self ):

        self.text = ""
        self.text_trans = ""
        self.first_lang = ""
        self.second_lang = ""
    

    def set_langs( self ):

        if not self.text:
            self.first_lang = constants.ARGUMENTS[2].value
            self.second_lang = constants.ARGUMENTS[3].value


    def set_text( self, text ):

        self.text = text
    

    def set_text_trans( self, text ):

        self.text_trans = text


    def set_first_lang( self, lang ):

        self.first_lang = lang


    def set_second_lang( self, lang ):

        self.second_lang = lang



class Translator:
    
    def __init__( self, transfv ):
        self.dest = constants.FIRST_LANG
        self.translator = googletrans.Translator()
        self.history = History()
        self.transfv = transfv


    def clear( self ):

        self.history.__init__()


    def check_more_words( self ):
        rawText = input( constants.INPUT ).split()
        i_last = len( rawText ) - 1

        if i_last == 0:
            self.one_word( rawText )
        elif i_last == -1:
            self.transfv.checkFunction( constants.CLEAR )
        else:
            self.more_words( rawText, i_last )


    def one_word( self, raw_text ):
        text = ' '.join( raw_text )
        if self.transfv.checkFunction( text ):
            return

        self.history.set_text( text )
        self.translate( text )
    

    def more_words( self, raw_text, i_last ):
        text_func = raw_text[ i_last ]

        isHaveFunc = False
        if self.transfv.checkFunction( text_func, False ):

            # Have func
            self.transfv.checkFunction( constants.CLEAR )
            del raw_text[ i_last ]
            isHaveFunc = True

        text = ' '.join( raw_text )
        self.history.set_text( text )
        self.translate( text )

        if isHaveFunc:
            self.transfv.checkFunction( text_func )


    def translation_loop( self ):

        while( True ):
            self.check_more_words()
    

    def translate( self, text ):

        if ( not text ):
            return

        self.transfv.prints.print_loading()

        translate = ""
        try:
            dest = self.detectDect( text )
            translate = self.translator.translate( text, dest=dest ).text
        except Exception as e:

            self.clear()

            message = getattr( e, 'message', str(e) )
            self.transfv.prints.print_error( message )
            return

        self.transfv.prints.print_trans( text, translate )
        self.history.set_text_trans( translate )


    def detectDect( self, text ):

        dest = self.translator.detect( text ).lang
        self.history.set_first_lang( dest )

        first = constants.ARGUMENTS[2]
        second = constants.ARGUMENTS[3]

        if ( dest == first.value ):
            dest = second.value
        elif ( dest == second.value ):
            dest = first.value

        self.history.set_second_lang( dest )
        
        return dest
