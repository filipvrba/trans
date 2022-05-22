from . import constants
import webbrowser

class ThirdSide:

    def open_google( self, history ):

        if ( history.second_lang != constants.CS_NAME ):
            return True  # Just end this a method, and continue function for print a message.

        uri = f"https://www.google.com/search?q={ history.text_trans }+v%C3%BDznam"
        webbrowser.open( uri )
        return False


    def open_google_trans( self, history ):

        uri = self.get_uri_google_trans( history )
        webbrowser.open( uri )


    def get_uri_google_trans( self, history ):

        history.set_langs()

        text = history.text
        if not text:
            text = ""

        return f"{ constants.URI_GOOGLE_TRANS }?sl={ history.first_lang }&tl={ history.second_lang }&text={ text }&op=translate"