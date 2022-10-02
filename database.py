from tinydb import TinyDB

class User:
    
    def __init__(self, username: str) -> None:
        """ initializ creating json file using user name
        """
        self.db = TinyDB(username + '.json', indent=4, separators=(',', ':'))
    
    def create_or_get_pl(self, playlistname):
        """Gets or creates table for playlist

        Args:
            playlistname (str): a playlist name

        Returns:
            Table: Return table object for given name
        """
        return self.db.table(playlistname)
    
    def all_pl(self) -> list:
        """Gets all playlist in username.json

        Returns:
            list: all playlist objects name
        """
        return list(self.db.tables())
    
    