import logging  

class BotDB:
    def __init__(self):
        import sqlite3 as sql
        logging.debug("Initializing Database...")

        self.connection = sql.connect("bot.db")
        self.cursor = self.connection.cursor()

