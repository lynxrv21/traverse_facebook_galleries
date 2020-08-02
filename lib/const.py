from enum import Enum


class Galleries(Enum):
    """ Image dict data.

    The gallery data can be a string or an object.
    If an object is provided, these are the data that it can contain. """

    URL = "url"
    COMMENT = "comment"
    SKIP = "skipped"


class Files(Enum):
    """ Names of the report files in each directory. """
    CAPTIONS = "captions.txt"
    DATA = "data.json"
    URLS = "urls.txt"
    OPTIONS = "options.json"
    OPTIONS_TEMPLATE = "options_template.json"


class Opt(Enum):
    """ Option variable names. """
    COOKIES = "cookies"
    SAVE_IMAGE_INDEX = "save_image_index"
    START_IMAGES = "start_images"
    MAX_WORKERS = "max_workers"
    DESTINATION = "destination_dir"
    USERNAME = "username"
    PASSWORD = "password"
    LOGIN = "force_login"
    BASE_URL = "loginURL"
    UNIQUE_GALLERIES = "unique_galleries"


class Selectors(Enum):
    """ Selectors for the elements of the ui """
    AUTH_EMAIL = "email"
    AUTH_PASS = "pass"
    AUTH_BUTTON = "loginbutton"
    NEXT_BUTTON = "a.next"
    IMAGE = "spotlight"
    POST_TIME = "#fbPhotoSnowliftTimestamp abbr"
    CAPTION = "fbPhotosPhotoCaption"
    GALLERY_NAME = ".fbPhotoMediaTitleNoFullScreen a"
    FULLSCREEN = "fbPhotoSnowliftFullScreenSwitch"
