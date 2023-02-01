import logging  

class BotDB:
    def __init__(self, db_name):
        import sqlite3 as sql
        logging.debug("Initializing Database...")

        self.connection = sql.connect("bot.db")
        self.cursor = self.connection.cursor()

