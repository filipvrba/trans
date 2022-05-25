from .argument import Argument

IS_DEBUG = False
GET = 'get'
SET = 'set'
SHORT = ':'
LONG = '='

APP = "trans"

EXIT = "exit()"
CLEAR = "clear()"
INFO = "info()"
OPEN = "#open"
OPEN_ALL = "open@"
OPEN_TWO = "open#"
HELP = "help()"
VALUE = "#value"
IMAGES = "#images"

CS_NAME = "cs"
FIRST_LANG = CS_NAME
SECOND_LANG = "en"
FIRST_LANG_NAME = "first"
SECOND_LANG_NAME = "second"
LANGUAGE_NAME = "languages"
SETTINGS_FILE = "settings.cfg"
URI_GOOGLE_TRANS = "https://translate.google.com/"

INPUT = ">>> "
LOADING = "..."
LAST_LINE = "\r"

ERROR_ICON = "[x]"
ARGUMENTS = [

    Argument( 'h', 'help', 'Print this help text and exit' ),
    Argument( 'm', 'message', 'The message is for translation.', SET ),
    Argument( 'f', 'first', 'Set a first language (example: "cs" or "en" ).', SET ),
    Argument( 's', 'second', 'Set a second language (example: "en" or "cs" ).', SET ),
    Argument( 'o', 'open', 'Open a web browser, with a translator tab.' ),
    Argument( 'v', 'value', 'Open a web browser, with a value word tab.' ),
    Argument( 'i', 'images', 'Open a web browser, with a images tab.' ),
    Argument( '', 'info', 'Print informations for this an app.' ),
]
