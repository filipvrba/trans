from . import constants
import webbrowser

class ThirdSide:

    def open_google( self, history ):

        uri = self.get_uri_google_trans( history )
        webbrowser.open( uri )


    def get_uri_google_trans( self, history ):

        history.set_langs()

        return f"{ constants.URI_GOOGLE_TRANS }?sl={ history.first_lang }&tl={ history.second_lang }&text={ history.text }&op=translate"