import logging  

class BotDB:
    def __init__(self):
        import sqlite3 as sql
        logging.debug("Initializing Database...")

        self.connection = sql.connect("bot.db")
        self.connection.execute('''CREATE TABLE IF NOT EXISTS guilds(
            guild_id INTEGER NOT NULL,
            carrier_channel_id INTEGER NOT NULL,
            carrier_id INTEGER NOT NULL,
            PRIMARY KEY (guild_id, carrier_channel_id, carrier_id));''')
        self.cursor = self.connection.cursor()

