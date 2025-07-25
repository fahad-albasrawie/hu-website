import os


class AdminDbConfiguration:
    DB_HOSTNAME = '104.237.2.47'
    DB_USERNAME = 'fahad'
    DB_NAME = 'hu_article'
    DB_PASSWORD = 'Assaamarraaii!@12'


class ArticleDbConfiguration:
    DB_HOSTNAME = '104.237.2.47'
    DB_USERNAME = 'fahad'
    DB_NAME = 'hu_article'
    DB_PASSWORD = 'Assaamarraaii!@12'


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
