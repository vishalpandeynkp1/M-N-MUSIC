import json
import os

YOUTUBE = {
    "access_token": "ya29.a0AeDClZC0ioRDkupmSNP9ueWqrfL8pvQLjxeIsOgScTVUWhLjjFU7VjljjWiqKX-8PdRDvl8EgQQ4T5oa9uFWiOnh0Iak3N0GkVjSIa0wI8xHCcW6S85nOKai6aqhf5-m-G9aj7iY7yxAD4eNFdtyyL8mbC5OcDDHGewnzAHsIZLac6iqElboaCgYKAYESARISFQHGX2Mi353nUd3LaexZeM_8bT6t4A0187",
    "expires": 1730084689.231148,
    "token_type": "Bearer",
    "refresh_token": "1//05vYI0c8OP0b4CgYIARAAGAUSNwF-L9IrJvP8EzLj-4wkJD-hYD9y1fXRNSGS9CjEQ1YwRxFw1OjatSgXsGooDbs5QcqAPOs3TvM"
}


def badmunda():
    TOKEN_DATA = os.getenv("TOKEN_DATA")
    if not TOKEN_DATA:
        os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
