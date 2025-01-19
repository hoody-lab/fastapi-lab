class BaseRepository():
    def __init__(self):
        self.db = Session = Depends(connect_database)