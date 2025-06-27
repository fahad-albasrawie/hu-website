import os


class AdminDbConfiguration:
    DB_HOSTNAME = '185.7.81.97'
    DB_USERNAME = 'fahad'
    DB_NAME = 'albasrawie'
    DB_PASSWORD = 'Assaamarraaii!@12'
    EMAIL_PASS = 'ukcbzrabhzzmvhcz'
    FROM_EMAIL = 'albasrawie.cs.edu@gmail.com'
    TO_EMAIL = 'cabbaascadde55@gmail.com'

class ArticleDbConfiguration:
    DB_HOSTNAME = '185.7.81.97'
    DB_USERNAME = 'fahad'
    DB_NAME = 'maqaal'
    DB_PASSWORD = 'Assaamarraaii!@12'
    EMAIL_PASS = 'ukcbzrabhzzmvhcz'
    FROM_EMAIL = 'albasrawie.cs.edu@gmail.com'
    TO_EMAIL = 'cabbaascadde55@gmail.com'

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
    DEBUG = os.environ.get("FLASK_DEBUG", "False").lower() in ("true", "1", "yes", "y", "on", "t")
    CROSS_ORIGINS = os.environ.get("CROSS_ORIGINS", "*") # or "http://localhost:5000" # Defines which domains can connect to my websocket server

    # Chat rooms
    CHAT_ROOMS = [
        "General",
        "Zero to Knowing",
        "Code with Josh",
        "Albasrawie"
    ]
