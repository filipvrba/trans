from . import constants

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